import json
import yaml
import uuid
import datetime
import sys

def readYamlSchemaFile(yamlFilePath):
    with open(yamlFilePath, "r") as file:
        return yaml.safe_load(file)

def getClassUri(_class, yamlSchemaDict):
    yamlShcemaClassesDict = yamlSchemaDict["classes"]
    return yamlShcemaClassesDict[_class]["class_uri"]

def getAttributeDict(_class, attribute, yamlShcemaClassesDict):
    if "attributes" not in yamlShcemaClassesDict[_class]:
        # print("No attributes")
        return None
    elif yamlShcemaClassesDict[_class]["attributes"] == None or attribute not in yamlShcemaClassesDict[_class]["attributes"]:
        # print("No attribute")
        return None
    elif yamlShcemaClassesDict[_class]["attributes"][attribute] == None or "slot_uri" not in yamlShcemaClassesDict[_class]["attributes"][attribute]:
        # print("No slot_uri")
        return None
    else:
        attributeDict = {}
        attributeDict["slot_uri"] = yamlShcemaClassesDict[_class]["attributes"][attribute]["slot_uri"]
        attributeDict["class"] = _class
        return attributeDict

def getAttributeRanges(_class, yamlShcemaClassesDict):
    rangeClassSet = set()
    if "attributes" not in yamlShcemaClassesDict[_class]:
        return rangeClassSet
    if yamlShcemaClassesDict[_class]["attributes"] == None:
        return rangeClassSet
    for attribute in yamlShcemaClassesDict[_class]["attributes"]:
        attributeDict = yamlShcemaClassesDict[_class]["attributes"][attribute]
        if "range" in attributeDict and attributeDict != None:
            if attributeDict["range"] in yamlShcemaClassesDict:
                rangeClassSet.add(yamlShcemaClassesDict[_class]["attributes"][attribute]["range"])
    return rangeClassSet

def getClassInheritage(_class, yamlShcemaClassesDict):
    inheritageSet = set()
    mixinsSet = set()
    if "is_a" in yamlShcemaClassesDict[_class]:
        inheritageSet.add(yamlShcemaClassesDict[_class]["is_a"])
    if "mixins" in yamlShcemaClassesDict[_class]: 
        for mixin in yamlShcemaClassesDict[_class]["mixins"]:
            inheritageSet.add(mixin)
            mixinsSet.add(mixin)
    inheritageSet.update(getAttributeRanges(_class, yamlShcemaClassesDict))
    inheritageDict = {"inheritageSet": inheritageSet, "mixinsSet": mixinsSet}
    return inheritageDict

def dfsInheritageClass(visitedSet, graphDict, node, mixinsSet):
  if node not in visitedSet:
    visitedSet.add(node)
    inheritageDict = getClassInheritage(node, graphDict)
    neighbours = inheritageDict["inheritageSet"]
    mixinsSet.update(inheritageDict["mixinsSet"])
    for neighbour in neighbours:
        dfsInheritageClass(visitedSet, graphDict, neighbour, mixinsSet)

def dfsInheritageAttribute(visitedSet, graphDict, node, attribute):
    # Check if the current node has the attribute
    attributeDict = getAttributeDict(node, attribute, graphDict)
    # If the node is not visited
    if node not in visitedSet:
        visitedSet.add(node)
        # Get inheritance information for the current node
        inheritageDict = getClassInheritage(node, graphDict)
        neighbours = inheritageDict["inheritageSet"]
        
        # Check if the current node has a valid slot_uri, and return if it exists
        if attributeDict is not None:
            return attributeDict
        
        # If no slot_uri, check the neighbours recursively
        for neighbour in neighbours:
            result = dfsInheritageAttribute(visitedSet, graphDict, neighbour, attribute)
            if result is not None:
                return result
    
    return None  # Return None if no valid slot_uri is found

def addSetToList(_lsit, _set):
    for item in _set:
        _lsit.append(item)

# Need to add check for mixin attributes. If they are not used in data @type should only contain one Class Uri
def returnType(_class, yamlSchemaDict):
    yamlShcemaClassesDict = yamlSchemaDict["classes"]
    _class = _class
    visitedSet = set()
    mixinsSet = set()
    dfsInheritageClass(visitedSet, yamlShcemaClassesDict, _class, mixinsSet)
    typeList = [_class]
    addSetToList(typeList, mixinsSet)
    typeUriList = []
    for _type in typeList:
        typeUriList.append(getClassUri(_type, yamlSchemaDict))  
    if len(typeUriList) == 1:
        return typeUriList[0]
    else:
        return typeUriList

def returnAttribute(_class, attribute, yamlSchemaDict):
    yamlShcemaClassesDict = yamlSchemaDict["classes"]
    visitedSet = set()
    attributeDict = dfsInheritageAttribute(visitedSet, yamlShcemaClassesDict, _class, attribute)
    return attributeDict

# Should be able to handle nested dictionaries with recursion
def cimDictHandling(value, _class, yamlSchemaDict):
    innerDict = {}
    for key, value in value.items():
        if key == "mRID":
            innerDict["@id"] = f"urn:uuid:{value}"
        else:
            innerDict[returnAttribute(_class, key, yamlSchemaDict)["slot_uri"]] = value
    return innerDict

def cimListHandling(values, _class, key, yamlSchemaDict):
    innerList = []
    for value in values:
        innerDict = {}
        if isinstance(value, dict):
            innerDict = cimDictHandling(value, _class, yamlSchemaDict)
        else:
            innerDict[returnAttribute(_class, key, yamlSchemaDict)] = value
        innerList.append(innerDict)
    return innerList

def createContext(yamlSchemaDict):
    context = {}
    context["@context"] = yamlSchemaDict["prefixes"]
    context["@context"].pop("linkml", None)
    context["@context"].pop("this", None)
    return context

def createJsonOutput(graphList, context, yamlSchemaDict):
    jsonOutput = {}
    documentUuid = str(uuid.uuid4())
    dateTimeUtcNow = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    jsonOutput["@context"] = context["@context"]

    jsonOutput["@id"] = f"urn:uuid:{documentUuid}"
    jsonOutput["@type"] = "dcat:Dataset"

    jsonOutput["prov:generatedAtTime"] = {}
    jsonOutput["prov:generatedAtTime"]["@value"] = dateTimeUtcNow
    jsonOutput["prov:generatedAtTime"]["@type"] = "xsd:date"

    jsonOutput["dcterms:title"] = yamlSchemaDict["dcterms"]["title"]

    jsonOutput["dcterms:description"] = []
    dcterms_description = {}
    dcterms_description["@value"] = yamlSchemaDict["dcterms"]["description"]
    dcterms_description["@language"] = "en"
    jsonOutput["dcterms:description"].append(dcterms_description)

    jsonOutput["dcterms:publisher"] = {}
    # jsonOutput["dcterms:publisher"]["@id"] = yamlSchemaDict["dcterms"]["publisherid"] # "urn:uuid:bd53cf0a-2e2f-4230-a591-0233290b5f9b"
    jsonOutput["dcterms:publisher"]["dcterms:title"] = yamlSchemaDict["dcterms"]["publisher"]

    jsonOutput["dcterms:temporal"] = {}
    jsonOutput["dcterms:temporal"]["@type"] = "dcterms:PeriodOfTime"
    dcterms_temporal_dcat_startDate = {}
    dcterms_temporal_dcat_startDate["@value"] = dateTimeUtcNow
    dcterms_temporal_dcat_startDate["@type"] = "xsd:dateTime"
    jsonOutput["dcterms:temporal"]["dcat:startDate"] = dcterms_temporal_dcat_startDate

    jsonOutput["dcterms:rights"] = yamlSchemaDict["dcterms"]["rights"][1:] #"© 2024 Copyright" need to check if the string contains copyright symbol and do some tweaks
    jsonOutput["dcterms:rightsHolder"] = yamlSchemaDict["dcterms"]["rightsHolder"]

    jsonOutput["dcterms:license"] = {}
    # jsonOutput["dcterms:license"]["@id"] = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
    jsonOutput["dcterms:license"]["dcterms:title"] = yamlSchemaDict["dcterms"]["license"]

    jsonOutput["dcterms:accessRights"] = {}
    # jsonOutput["dcterms:accessRights"]["@id"] = "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
    jsonOutput["dcterms:accessRights"]["dcterms:title"] = yamlSchemaDict["dcterms"]["accessRights"]

    jsonOutput["dcterms:isVersionOf"] = {}
    jsonOutput["dcterms:isVersionOf"]["@id"] = yamlSchemaDict["dcterms"]["isVersionOf"]

    jsonOutput["dcat:keyword"] = yamlSchemaDict["dcat"]["keyword"]

    jsonOutput["dcterms:spatial"] = {}
    jsonOutput["dcterms:spatial"]["@id"] = yamlSchemaDict["dcterms"]["spatial"]

    jsonOutput["dcterms:conformsTo"] = []
    for object in yamlSchemaDict["dcterms"]["conformsTo"]:
        dcterms_conformsTo = {}
        dcterms_conformsTo["@id"] = object
        jsonOutput["dcterms:conformsTo"].append(dcterms_conformsTo)

    jsonOutput["dcterms:references"] = []
    for object in yamlSchemaDict["dcterms"]["references"]:
        dcterms_reference = {}
        dcterms_reference["@id"] = object
        jsonOutput["dcterms:references"].append(dcterms_reference)

    jsonOutput["@graph"] = graphList

    return jsonOutput

def isEnum(initialClass, attribute, value, yamlSchemaDict):

    _class = returnAttribute(initialClass, attribute, yamlSchemaDict)["class"]

    if "classes" not in yamlSchemaDict or yamlSchemaDict["classes"] == None:
        return {"value": value, "isEnum": False}
    
    if _class not in yamlSchemaDict["classes"] or yamlSchemaDict["classes"][_class] == None:
        return {"value": value, "isEnum": False}
    
    if "attributes" not in yamlSchemaDict["classes"][_class] or yamlSchemaDict["classes"][_class]["attributes"] == None:
        return {"value": value, "isEnum": False}
    
    if attribute not in yamlSchemaDict["classes"][_class]["attributes"] or yamlSchemaDict["classes"][_class]["attributes"][attribute] == None:
        return {"value": value, "isEnum": False}

    if "range" not in yamlSchemaDict["classes"][_class]["attributes"][attribute] or yamlSchemaDict["classes"][_class]["attributes"][attribute]["range"] == None:
        return {"value": value, "isEnum": False}

    _range = yamlSchemaDict["classes"][_class]["attributes"][attribute]["range"]

    if "enums" not in yamlSchemaDict or yamlSchemaDict["enums"] == None:
        return {"value": value, "isEnum": False}
    
    if _range not in yamlSchemaDict["enums"] or yamlSchemaDict["enums"][_range] == None:
        return {"value": value, "isEnum": False}

    if "permissible_values" not in yamlSchemaDict["enums"][_range] or yamlSchemaDict["enums"][_range]["permissible_values"] == None:
        return {"value": value, "isEnum": False}

    if value not in yamlSchemaDict["enums"][_range]["permissible_values"] or yamlSchemaDict["enums"][_range]["permissible_values"][value] == None:
        return {"value": value, "isEnum": False}

    if "meaning" not in yamlSchemaDict["enums"][_range]["permissible_values"][value] or yamlSchemaDict["enums"][_range]["permissible_values"][value]["meaning"] == None:
        return {"value": value, "isEnum": False}

    meaningValue = yamlSchemaDict["enums"][_range]["permissible_values"][value]["meaning"]
    return {"value": meaningValue, "isEnum": True}

# Need to rewrite this
def yamlToJsonldConverter(yamlSchemaFilePath, yamlDataFilePath, outputFilePath):
    yamlSchemaDict = readYamlSchemaFile(yamlSchemaFilePath)
    yamlDataDict = readYamlSchemaFile(yamlDataFilePath)
    graphList = []
    for _class in yamlDataDict:
        for object in yamlDataDict[_class]:
            classDict = {}
            _count = 0
            for key, value in object.items():
                if key == "mRID":
                    classDict["@id"] = f"urn:uuid:{value}"
                if _count == 0:
                    classDict["@type"] = returnType(_class, yamlSchemaDict)
                
                if isinstance(value, dict):
                    innerDict = cimDictHandling(value, _class, yamlSchemaDict)
                    classDict[returnAttribute(_class, key, yamlSchemaDict)["slot_uri"]] = innerDict
                elif isinstance(value, list):
                    innerDict = cimListHandling(value, _class, key, yamlSchemaDict)
                    classDict[returnAttribute(_class, key, yamlSchemaDict)["slot_uri"]] = innerDict
                elif isEnum(_class, key, value, yamlSchemaDict)["isEnum"] == True:
                    classDict[returnAttribute(_class, key, yamlSchemaDict)["slot_uri"]] = {"@id": isEnum(_class, key, value, yamlSchemaDict)["value"]}
                else:
                    classDict[returnAttribute(_class, key, yamlSchemaDict)["slot_uri"]] = value
                _count += 1
            graphList.append(classDict)

    outputJson = createJsonOutput(graphList, createContext(yamlSchemaDict), yamlSchemaDict)

    with open(outputFilePath, "w", encoding="utf-8") as jsonFile:
        json.dump(outputJson, jsonFile, indent=4, ensure_ascii=False)

# Variables
# yamlSchemaFilePath = "AO_schema.yaml"
# yamlDataFilePath = "AO.yaml"
# outputFilePath = "AO_created_from_code.jsonld"

# yamlToJsonldConverter(yamlSchemaFilePath, yamlDataFilePath, outputFilePath)

if __name__ == "__main__":
    yamlSchemaFilePath = sys.argv[1] if len(sys.argv) > 1 else None
    yamlDataFilePath = sys.argv[2] if len(sys.argv) > 2 else None
    outputFilePath = sys.argv[3] if len(sys.argv) > 3 else None
    yamlToJsonldConverter(yamlSchemaFilePath, yamlDataFilePath, outputFilePath)

# Missing:
## yamlToJsonldConverter - Need to rewrite this
## cimDictHandling - Should be able to handle nested dictionaries with recursion
## returnType - Need to add check for mixin attributes. If they are not used in data @type should only contain one Class Uri
## createJsonOutput - Missing @id for dcterms:publisher, dcterms:license, dcterms:accessRights
## missing so if checks overal so some dict lookups will fail. Look to isEnum where i have done all the if checks
## It does not support to have a nested enum
## It should not use mixins if non attributes from that is used for type
## It should use python classes