import click
from python.jsonldFromYamlConverter import yamlToJsonldConverter
from python.generalFunctions import run_bash_command, to_camel_case, remove_all_md_files
from python.replace_star_with_0dotdotstar import traverse_and_replace
import uuid
from python.createmd import CreateMdController
from python.createOverviewMd import CreaeOverviewMdController

@click.group()
def main():
    pass

@main.command()
@click.argument('text')
def hello(text: str):
    '''Say Hello to the user'''
    click.echo(f'Hello {text}!')

@main.command()
@click.option('--schema', '-s', required=True, default=None, help='YAML Schema file name to use')
def docs(schema: str):
    '''Create Documentation from yaml schemas'''
    click.echo('Creating Documentation')
    _schema = f'schemas/yaml/{schema}.linkml.yaml'
    docs = to_camel_case(schema)

    run_bash_command(f"rm docs/{docs}/*.md", f"Remove old documentation for {_schema}")
    run_bash_command(f"gen-doc -d docs/{docs} --diagram-type mermaid_class_diagram --template-directory _templates/ --use-slot-uris {_schema}", f"Create documentation for {_schema}")

    traverse_and_replace('docs/', ' | * ', ' | 0..* ')
    click.echo('Replaced * with 0..* in all .md files in docs/')

@main.command()
@click.option('--schema', '-s', required=True, default=None, help='YAML Schema file name to use')
def genDocs(schema: str):
    '''Generate Documentation from yaml schemas using python'''
    click.echo('Generating Documentation using python')
    remove_all_md_files(f"docs/{to_camel_case(schema)}")
    CreateMdController().main(schema)
    click.echo('Generating Overview index.md')
    CreaeOverviewMdController().main()
    click.echo('Overview index.md Created')
    
@main.command()
@click.option('--number', '-n', required=False, default=1, type=int, help='Number of uuids you want')
def uuidv4(number: int):
    '''Generate UUIDv4'''
    for i in range(0, number):
        click.echo(uuid.uuid4())

@main.command()
@click.option('--schema', '-s', required=False, default=None, type=str, help='YAML Schema file name to use')
@click.option('--data', '-d', required=False, default=None, type=str, help='YAML Data file name to use')
@click.option('--output', '-o', required=False, default=None, type=str, help='Output file name')
@click.option('--filename', '-f', required=False, default=None, type=str, help='file name, if you provide this all files will have the same name. This should be the same as the yaml schema name and data name')
def JsonLD(schema: str, data: str, output: str, filename: str):
    '''Convert YAML to JSON-LD'''
    click.echo('Converting YAML to JSON-LD')
    if filename != None:
        _schema = f'schemas/yaml/{filename}.linkml.yaml'
        _data = f'data/yaml/{filename}.yaml'
        _output = f'data/jsonld/{filename}.jsonld'
        click.echo(f'Converting {_schema} and {_data} to {_output}')
        yamlToJsonldConverter(_schema, _data, _output)
        return
    elif (schema != None and data != None and output != None):
        _schema = f'schemas/yaml/{schema}.linkml.yaml'
        _data = f'data/yaml/{data}.yaml'
        _output = f'data/jsonld/{output}.jsonld'
        click.echo(f'Converting {_schema} and {_data} to {_output}')
        yamlToJsonldConverter(_schema, _data, _output)
        return
    else:
        click.echo('Please provide the schema, data and output file names or the filename')
        return

@main.command()
def run_local_app():
    '''Run the local app'''
    click.echo('Run this command in terminal: mkdocs serve')

@main.command()
@click.option('--schema', '-s', required=True, default=None, help='YAML Schema file name to use')
def createJsonSchema(schema: str):
    '''Create Json Schema from Yaml Schema'''
    run_bash_command(f"gen-json-schema schemas/yaml/{schema}.linkml.yaml > schemas/json/{schema}_schema.json", "Create Json Schema from Yaml Schema")

if __name__ == '__main__':
    main()
