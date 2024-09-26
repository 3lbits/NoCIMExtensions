import json
import yaml
import sys

def readJsonFile(jsonldFilePath):
    with open(jsonldFilePath, "r") as file:
        return json.load(file)

def readYamlSchemaFile(yamlFilePath):
    with open(yamlFilePath, "r") as file:
        return yaml.safe_load(file)

def find_value_in_hierarchy(data_dict, current_class, current_attribute):
    
    # Does not support mxins atm
    if current_attribute in ("asWKT", "asGeoJSON", "asGML"): 
        current_class = "Geometry"
    if current_attribute in ("hasGeometry"):
        current_class = "SpatialObject"
    else:
        current_class = current_class
    
    current_attribute = current_attribute
    
    # Check if the target key exists at the current level
    if "attributes" in data_dict[current_class] or data_dict[current_class]["attributes"] == None:
        return None
    if current_attribute in data_dict[current_class]["attributes"]:
        return data_dict[current_class]["attributes"][current_attribute]["slot_uri"]
    
    if "is_a" in data_dict[current_class]:
        current_class = data_dict[current_class].get("is_a")
    
        # Recursively call the function with the next key
        return find_value_in_hierarchy(data_dict, current_class, current_attribute)
    else:
        return None

def getClassUri(_class, yamlSchemaDict):
    return yamlSchemaDict["classes"][_class]["class_uri"]

def createValue(_class, key, value, yamlSchemaDict, data):
    if find_value_in_hierarchy(yamlSchemaDict["classes"], _class, key) == None:
        return None
    if "@context" in data["@context"][key]:
        prefix = find_value_in_hierarchy(yamlSchemaDict["classes"], _class, key).split(':')[0]
        keyName = key.capitalize()
        return {"@id": f"{prefix}:{keyName}.{value}"}
    elif isinstance(value, dict):
        keyValueDict = {}
        for subValue in value:
            keyValueDict[find_value_in_hierarchy(yamlSchemaDict["classes"], _class, subValue)] = value[subValue]
        return keyValueDict
    elif isinstance(value, list):
        keyValueList = []
        for subValue in value:
            print(value)
            print(type(value))
            print(subValue)
            print(type(subValue))
            subValue = subValue["mRID"]
            keyValueDict = {"@id": f"urn:uuid:{subValue}"}
            keyValueList.append(keyValueDict)
        return keyValueList
    else:
        return value

def getDataKeys(data):
    keyList = []
    for key in data.keys():
        if key not in ["@type", "@context"]:
            keyList.append(key)
    return keyList

def popUnwatedItems(unWantedContextItems, data):
    keys_to_remove = unWantedContextItems
    for key in data["@context"].keys():
        if isinstance(data["@context"][key], dict):
            keys_to_remove.append(key)
    for key in keys_to_remove:
        data["@context"].pop(key)

def generateId(attribute, attributes, classDict):
    if attribute == "mRID":
        classDict["@id"] = f"urn:uuid:{attributes[attribute]}"

def createGraphList(popSet, data, yamlSchemaDict):
    graph = []

    for cimClass in getDataKeys(data):
        popSet.add(cimClass)
        for attributes in data[cimClass]:
            classDict = {}
            for attribute in attributes:
                generateId(attribute, attributes, classDict)
                classDict["@type"] = getClassUri(cimClass, yamlSchemaDict)
                cimAttribute = find_value_in_hierarchy(yamlSchemaDict["classes"], cimClass, attribute)
                classDict[cimAttribute] = createValue(cimClass, attribute, attributes[attribute], yamlSchemaDict, data)
                popSet.add(attribute)
            graph.append(classDict)
    return graph

def writeJsonFile(outputFilePath, data):
    fileName = outputFilePath.rsplit('.', 1)[0]
    with open(f"{fileName}_Corrected.jsonld", 'w') as file:
        file.write(data)
    print(f"JSON-LD data successfully written to {fileName}_Corrected.jsonld")

def jsonldtransformer(outputFilePath, yamlSchemaFilePath):
    data = readJsonFile(outputFilePath)
    yamlSchemaDict = readYamlSchemaFile(yamlSchemaFilePath)
    popSet = set()
    graph = createGraphList(popSet, data, yamlSchemaDict)

    unWantedContextItems = [
        "linkml",
        "this",
        "@vocab",
    ]

    popUnwatedItems(unWantedContextItems, data)

    # Construct the final transformed structure
    transformed_data = {
        "@context": data["@context"],
        "@graph": graph
    }

    # Output the transformed data as JSON
    transformed_json_ld = json.dumps(transformed_data, indent=4)

    writeJsonFile(outputFilePath, transformed_json_ld)

# jsonldtransformer("AO.jsonld", "AO_schema.yaml")

if __name__ == "__main__":
    outputFilePath = sys.argv[1] if len(sys.argv) > 1 else None
    yamlSchemaFilePath = sys.argv[2] if len(sys.argv) > 2 else None
    jsonldtransformer(outputFilePath, yamlSchemaFilePath)