import click
import uuid
from cim4CLITool.jsonldFromYamlConverter import yamlToJsonldConverter
from cim4CLITool.generalFunctions import run_bash_command, to_camel_case, remove_all_md_files
from cim4CLITool.docs.main import CreateMdController
from cim4CLITool.createOverviewMd import CreateOverviewMdController
from cim4CLITool.xmlSorting import ControllerXmlSorting
import os

@click.group()
def main():
    '''
    Welcome to CIM4 CLI Tool                                                
    Powered by ElBits                                                       
    Inspired by LinkML                                                      
    '''
    pass

@main.group()
def xml():
    '''Group for XML related commands'''
    pass

@main.group()
def jsonld():
    '''Group for JSON-LD related commands'''
    pass

@main.group()
def json():
    '''Group for JSON related commands'''
    pass

@main.group()
def docs():
    '''Group for Documentation related commands'''
    pass

@main.command()
@click.option('--number', '-n', required=False, default=1, type=int, help='Number of uuids you want. If not provided, it will generate 1 uuid')
def uuidv4(number: int):
    '''Generate UUIDv4'''
    for i in range(0, number):
        click.echo(uuid.uuid4())

@docs.command()
@click.option('--schema', '-s', required=True, default=None, help='YAML Schema file name to use')
def gen(schema: str):
    '''Generate Documentation from yaml schemas using python'''
    click.echo('Generating Documentation using python')
    remove_all_md_files(f"docs/{to_camel_case(schema)}")
    CreateMdController().main(schema, template='elbits')
    click.echo('Generating Overview index.md')
    CreateOverviewMdController().main()
    click.echo('Overview index.md Created')

@docs.command()
def run_local_app():
    '''Run the local app'''
    click.echo('Run this command in terminal: mkdocs serve')

@jsonld.command()
@click.option('--schema', '-s', required=False, default=None, type=str, help='YAML Schema file name to use')
@click.option('--data', '-d', required=False, default=None, type=str, help='YAML Data file name to use')
@click.option('--output_file_name', '-o', required=False, default=None, type=str, help='Output file name')
@click.option('--file_name', '-f', required=False, default=None, type=str, help='file name, if you provide this all files will have the same name. This should be the same as the yaml schema name and data name')
def gen(schema: str, data: str, output_file_name: str, file_name: str):
    '''Convert YAML to JSON-LD'''
    click.echo('Converting YAML to JSON-LD')
    if file_name != None:
        _schema = f'schemas/yaml/{file_name}.linkml.yaml'
        _data = f'data/yaml/{file_name}.yaml'
        _output = f'data/jsonld/{file_name}.jsonld'
    elif (schema != None and data != None and output_file_name != None):
        _schema = f'schemas/yaml/{schema}.linkml.yaml'
        _data = f'data/yaml/{data}.yaml'
        _output = f'data/jsonld/{output_file_name}.jsonld'
    else:
        click.echo('Please provide the schema, data and output_file_name or the file_name')
        return
    
    click.echo(f'Converting {_schema} and {_data} to {_output}')
    yamlToJsonldConverter(_schema, _data, _output)

@xml.command()
@click.option('--file_name', '-f', required=False, default=None, help='XML file name to use')
@click.option('--input_path', '-i', required=False, default=None, help='Input file path to use')
@click.option('--output_path', '-o', required=False, default=None, help='Output file path to use')
@click.option('--cim4_formatting', '-c', required=False, default=False, is_flag=True, help='Use CIM4 formatting')
@click.option('--print_output', '-p', required=False, default=False, is_flag=True, help='Print output to console')
@click.option('--bulk', '-b', required=False, default=False, is_flag=True, help='Sort all XML files in the input folder')
def sort(file_name: str, input_path: str, output_path: str, cim4_formatting: bool, print_output: bool, bulk: bool):
    '''Sort XML file/files'''
    click.echo('Sorting XML file')

    if bulk:

        if input_path is None or not os.path.exists(input_path):
            click.echo('Input path does not exist. Please provide a valid input_path for bulk sorting.')
            return
        
        if output_path is not None and not os.path.exists(output_path):
            click.echo(f'Warning: Output path "{output_path}" does not exist.')
            proceed = click.confirm('Do you want to proceed anyway?', default=False)
            if not proceed:
                click.echo('Operation cancelled by user.')
                return

        if output_path is None:
            click.echo('output_path not provided. Using input_path as output_path.')
            output_path = input_path

        click.echo('Sorting all XML files in the input folder')
        ControllerXmlSorting.sort_multiple_files(input_path, output_path, print_output=print_output, cim4_formatting=cim4_formatting)
        click.echo(f'Sorted all XML files in {input_path} and saved to {output_path}')
        return

    if file_name != None:
        inputFilePath = f"data/xml/{file_name}.xml"
        outputFilePath = f"data/xml/{file_name}_sorted.xml"
    elif (input_path != None and output_path != None):
        inputFilePath = input_path
        outputFilePath = output_path
    else:
        click.echo('Please provide the file_name or input_path or input_path and output_path')
        return

    ControllerXmlSorting.sort_single_files(inputFilePath, outputFilePath, print_output=print_output, cim4_formatting=cim4_formatting)

    click.echo(f'Sorted XML file {inputFilePath} and saved to {outputFilePath}')

@json.command()
@click.option('--schema', '-s', required=True, default=None, help='YAML Schema file name to use')
def schema(schema: str):
    '''Create Json Schema from Yaml Schema (LinkML)'''
    run_bash_command(f"gen-json-schema schemas/yaml/{schema}.linkml.yaml > schemas/json/{schema}_schema.json", "Create Json Schema from Yaml Schema")

if __name__ == '__main__':
    main()
