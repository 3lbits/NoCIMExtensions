import yaml

class General:
    def read_yaml_to_dict(file_path):
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        return data
    
    def write_dict_to_yaml(file_path, data):
        with open(file_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)

if __name__ == "__main__":
    # Example usage
    inputFilePath = "schemas\yaml\cim_model.linkml.yaml"  # Replace with your XML file path
    outputFilePath = "schemas\yaml\cim_model_removed_duplicates.linkml.yaml"  # Replace with your desired output file path

    yamlDict = General.read_yaml_to_dict(inputFilePath)

    yamlOutputDict = General.read_yaml_to_dict(inputFilePath)

    classList = []
    enumList = []
    typeList = []

    for _class in yamlDict["classes"]:  # Iterate over a copy of the keys
        if _class.endswith("1"):
            yamlOutputDict["classes"].pop(_class)
            print(f"Removed Class: {_class}")
        else:
            classList.append(_class)

    for enum in yamlDict["enums"]:  # Iterate over a copy of the keys
        if enum.endswith("1"):
            yamlOutputDict["enums"].pop(enum)
            print(f"Removed Enum: {enum}")
        else:
            enumList.append(enum)
    
    for _type in yamlDict["types"]:  # Iterate over a copy of the keys
        if _type.endswith("1"):
            yamlOutputDict["types"].pop(_type)
            print(f"Removed Type: {_type}")
        else:
            typeList.append(_type)

    yamlDict["classes"] = classList
    yamlDict["enums"] = enumList
    yamlDict["types"] = typeList

    General.write_dict_to_yaml(outputFilePath, yamlOutputDict)