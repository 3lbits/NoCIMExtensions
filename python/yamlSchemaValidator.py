import yaml
from jsonschema import validate, ValidationError
import subprocess

# gen-json-schema schemas/wattapp.linkml.yaml > schemas/wattapp_schema.json
# Issue: When using any_of in yaml schema linkml creates a bug where you get an extra type

def run_bash_command(command, commandName):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{commandName} executed successfully.")
        print(result.stdout)
    else:
        print(f"{commandName} failed.")
        print(result.stderr)

def remove_type_keys_with_anyof(schema_file_path):
    with open(schema_file_path, 'r') as file:
        lines = file.readlines()
        line_index_anyOf = 1
        for line in lines:
            if "anyOf" in line:
                # print(line)
                number_of_spaces = line.find('"anyOf"')
                line_index_anyOf = lines.index(line)

        # print(lines[35])
        startingIndexes = [26, 82, 196] # Get this from looping trough all lines and store all lines containing "anyOf"
        indexesToRemove = [] #Remember to remove , on previous line if next line got a different number of spaces
        number_of_spaces = 0
        for startingIndex in startingIndexes:
            for index in range(startingIndex, len(lines)):
                if "anyOf" in lines[index]:
                    number_of_spaces = lines[index].find("anyOf") - 1
                    starting_spaces = len(lines[index]) - len(lines[index].lstrip())
                if len(lines[index]) - len(lines[index].lstrip()) < starting_spaces:
                    break
                if lines[index].startswith(f'{" " * number_of_spaces}"type": "string"'):
                    indexesToRemove.append({"index": index, "starting_spaces": starting_spaces})

                print(lines[index])

        print(indexesToRemove)

        for item in sorted(indexesToRemove, key=lambda x: x['index'], reverse=True):
            del lines[item['index']]

        with open(schema_file_path, 'w') as file:
            file.writelines(lines)

                # while next_line_index < len(lines):
                #     next_line = lines[next_line_index]
                #     print(number_of_spaces)
                #     print(next_line)
                #     # if next_line.startswith(' ' * number_of_spaces + "type: \"string\""):
                #     #     break
                #     if next_line.startswith(' ' * (number_of_spaces + 1)):
                #         next_line_index += 1
                #     else:
                #         break

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def load_json_schema(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def validate_yaml(yaml_data, schema):
    try:
        validate(instance=yaml_data, schema=schema)
        print("YAML data is valid.")
    except ValidationError as e:
        print(f"YAML data is invalid: {e.message}")

if __name__ == "__main__":
    yaml_file_path = "data/yaml/wattapp.yaml"
    schema_file_path = "schemas/wattapp_schema.json"

    yaml_data = load_yaml(yaml_file_path)
    json_schema = load_json_schema(schema_file_path)
    
    # Creating json schema from yaml schema using linkml
    # run_bash_command("gen-json-schema schemas/wattapp.linkml.yaml > schemas/wattapp_schema.json", "Create Json Schema from Yaml Schema")
    
    remove_type_keys_with_anyof("schemas/wattapp_schema.json")

    # Validate yaml data using json schema
    # validate_yaml(yaml_data, json_schema)