import click
from python.jsonldFromYamlConverter import yamlToJsonldConverter
from python.generalFunctions import run_bash_command, to_camel_case#, remove_files_matching_pattern
from python.replace_star_with_0dotdotstar import traverse_and_replace

@click.command()

@click.option('--type', '-t', required=True, default="JsonLD", help='Choose type of command to run. [JsonLD, Hello, Docs, DocApp]')

@click.option('--schema', '-s', required=False, default=None, help='YAML Schema file name to use')

@click.option('--data', '-d', required=False, default=None, help='YAML Data file name to use')

@click.option('--output', '-o', required=False, default=None, help='Output file name')

@click.option('--filename', '-f', required=False, default=None, help='file name, if you provide this all files will have the same name')


def cli(type: str, schema: str, data: str, output: str, filename: str):
    if type not in ['JsonLD', 'Hello', 'Docs', 'DocApp']:
        click.echo('Invalid type. Use --help to see available types')
        return
    if type == 'Hello':
        click.echo('Hello World')
        return

    if type == 'JsonLD':
        click.echo('Converting YAML to JSON-LD')
        if filename != None:
            _schema = f'schemas/{filename}.linkml.yaml'
            _data = f'data/yaml/{filename}.yaml'
            _output = f'data/jsonld/{filename}.jsonld'
            click.echo(f'Converting {_schema} and {_data} to {_output}')
            yamlToJsonldConverter(_schema, _data, _output)
            return
        elif (schema != None and data != None and output != None):
            _schema = f'schemas/{schema}.linkml.yaml'
            _data = f'data/yaml/{data}.yaml'
            _output = f'data/jsonld/{output}.jsonld'
            click.echo(f'Converting {_schema} and {_data} to {_output}')
            yamlToJsonldConverter(_schema, _data, _output)
            return
        else:
            click.echo('Please provide the schema, data and output file names or the filename')
            return

    if type == 'Docs':
        click.echo('Creating Documentation')
        _schema = f'schemas/{schema}.linkml.yaml'
        docs = to_camel_case(schema)

        run_bash_command(f"rm docs/{docs}/*.md", f"Remove old documentation for {_schema}")
        run_bash_command(f"gen-doc -d docs/{docs} --diagram-type mermaid_class_diagram --template-directory _templates/ --use-slot-uris {_schema}", f"Create documentation for {_schema}")

        traverse_and_replace('docs/', ' | * ', ' | 0..* ')
        click.echo('Replaced * with 0..* in all .md files in docs/')

        # remove_files_matching_pattern("docs", "^# (Slot|Type): ")

        # run_bash_command(grepCommand, f"Remove Slot and Type from documentation")
        return
    
    if type == 'DocApp':
        click.echo("Run this command in your terminal: mkdocs serve")
        return

	# gen-doc -d docs/AviationObstacle --diagram-type mermaid_class_diagram --template-directory _templates/ --use-slot-uris schemas/aviationobstacle.linkml.yaml
	# gen-doc -d docs/WattApp --diagram-type mermaid_class_diagram --template-directory _templates/ --use-slot-uris schemas/wattapp.linkml.yaml
	# grep -E '^# (Slot|Type): ' -lr --include \*.md docs | xargs -d '\n' rm
    # r"grep -E '^# (Slot|Type): ' -lr --include \*.md docs | xargs -d '\n' rm"

if __name__ == '__main__':
    cli()
