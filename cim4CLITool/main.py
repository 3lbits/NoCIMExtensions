import click
from cim4CLITool.jsonldFromYamlConverter import yamlToJsonldConverter
from cim4CLITool.generalFunctions import run_bash_command, to_camel_case, remove_all_md_files
from cim4CLITool.replace_star_with_0dotdotstar import traverse_and_replace
import uuid
from cim4CLITool.docs.main import CreateMdController
from cim4CLITool.createOverviewMd import CreaeOverviewMdController
from cim4CLITool.xmlSorting import ControllerXmlSorting

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
    CreaeOverviewMdController().main()
    click.echo('Overview index.md Created')

@docs.command()
def run_local_app():
    '''Run the local app'''
    click.echo('Run this command in terminal: mkdocs serve')

@jsonld.command()
@click.option('--schema', '-s', required=False, default=None, type=str, help='YAML Schema file name to use')
@click.option('--data', '-d', required=False, default=None, type=str, help='YAML Data file name to use')
@click.option('--output', '-o', required=False, default=None, type=str, help='Output file name')
@click.option('--filename', '-f', required=False, default=None, type=str, help='file name, if you provide this all files will have the same name. This should be the same as the yaml schema name and data name')
def gen(schema: str, data: str, output: str, filename: str):
    '''Convert YAML to JSON-LD'''
    click.echo('Converting YAML to JSON-LD')
    if filename != None:
        _schema = f'schemas/yaml/{filename}.linkml.yaml'
        _data = f'data/yaml/{filename}.yaml'
        _output = f'data/jsonld/{filename}.jsonld'
    elif (schema != None and data != None and output != None):
        _schema = f'schemas/yaml/{schema}.linkml.yaml'
        _data = f'data/yaml/{data}.yaml'
        _output = f'data/jsonld/{output}.jsonld'
    else:
        click.echo('Please provide the schema, data and output file names or the filename')
        return
    
    click.echo(f'Converting {_schema} and {_data} to {_output}')
    yamlToJsonldConverter(_schema, _data, _output)

@xml.command()
@click.option('--filename', '-f', required=False, default=None, help='XML file name to use')
@click.option('--input', '-i', required=False, default=None, help='Input file path to use')
@click.option('--output', '-o', required=False, default=None, help='Output file path to use')
@click.option('--cim4_formatting', '-c', required=False, default=False, is_flag=True, help='Use CIM4 formatting')
@click.option('--print_output', '-p', required=False, default=False, is_flag=True, help='Print output to console')
def sort(filename: str, input: str, output: str, cim4_formatting: bool, print_output: bool):
    '''Sort XML file'''
    click.echo('Sorting XML file')

    if filename != None:
        inputFilePath = f"data/xml/{filename}.xml"
        outputFilePath = f"data/xml/{filename}_sorted.xml"
    elif (input != None and output != None):
        inputFilePath = input
        outputFilePath = output
    else:
        click.echo('Please provide the filename or input and output file paths')
        return

    if cim4_formatting:
        click.echo('Using CIM4 formatting')
        if print_output:
            click.echo('Printing output to console')
            ControllerXmlSorting.main(inputFilePath, outputFilePath, print_output=True, cim4_formatting=True)
        else:
            ControllerXmlSorting.main(inputFilePath, outputFilePath, print_output=False, cim4_formatting=True)
    else:
        if print_output:
            click.echo('Printing output to console')
            ControllerXmlSorting.main(inputFilePath, outputFilePath, print_output=True, cim4_formatting=False)
        else:
            ControllerXmlSorting.main(inputFilePath, outputFilePath, print_output=False, cim4_formatting=False)

    click.echo(f'Sorted XML file {inputFilePath} and saved to {outputFilePath}')

@json.command()
@click.option('--schema', '-s', required=True, default=None, help='YAML Schema file name to use')
def schema(schema: str):
    '''Create Json Schema from Yaml Schema (LinkML)'''
    run_bash_command(f"gen-json-schema schemas/yaml/{schema}.linkml.yaml > schemas/json/{schema}_schema.json", "Create Json Schema from Yaml Schema")

if __name__ == '__main__':
    main()
