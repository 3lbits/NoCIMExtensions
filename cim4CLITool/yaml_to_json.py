import yaml
import json

class GeneralUtils:

    @staticmethod
    def read_yaml_file(file_path):
        with open(file_path, 'r') as file:
            try:
                data = yaml.safe_load(file)
                return data
            except yaml.YAMLError as e:
                print(f"Error reading YAML file: {e}")
                return None
            
    @staticmethod
    def write_dict_to_json(data, file_path, pretty_print=True, print_json=True):
        try:
            with open(file_path, 'w') as file:

                if pretty_print:
                    json.dump(data, file, indent=4)
                else:
                    json.dump(data, file)
                
                print(f"JSON data successfully written to {file_path}")

                if print_json:
                    print(json.dumps(data, indent=4))

        except Exception as e:
            print(f"Error writing JSON file: {e}")

class ControllerYamlToJson:

    def yaml_to_json(input_file_path, output_file_path, pretty_print=True, print_json=True):

        data = GeneralUtils.read_yaml_file(input_file_path)
        GeneralUtils.write_dict_to_json(data, output_file_path, pretty_print, print_json)


if __name__ == "__main__":
    # Example usage
    input_file_path = 'data/yaml/watt_app.yaml'  # Replace with your YAML file path
    output_file_path = 'data/json/watt_app.json'  # Replace with your desired JSON file path
    ControllerYamlToJson.yaml_to_json(input_file_path, output_file_path, pretty_print=True, print_json=True)