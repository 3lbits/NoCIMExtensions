import yaml
import os
from cim4CLITool.docs.templates import TemplateClass, EditMkDocsYaml
from cim4CLITool.docs.configs.mkdocs_config import MkDocsConfig

class mkdocs:

    def mkdocs_profile_index():

        title = globalYamlDict["title"] if "title" in globalYamlDict else "No title available"
        name = globalYamlDict["name"] if "name" in globalYamlDict else "No name available"
        description = globalYamlDict["comments"] if "comments" in globalYamlDict else "No description available"

        profile_index_dict = {
            'title': title,
            'name': name,
            'description': description,
        }

        abstractClasses = []
        concreteClasses = []
        enumerations = []
        types = []

        for _class in globalYamlDict["classes"]:
            if 'abstract' in globalYamlDict["classes"][_class] and globalYamlDict["classes"][_class]['abstract'] == True:
                abstractClasses.append({'name': _class, 'path': f'{globalLookUpDataDict[_class]["absoluteUrlPath"]}'})
            if 'abstract' in globalYamlDict["classes"][_class] and globalYamlDict["classes"][_class]['abstract'] == False or 'abstract' not in globalYamlDict["classes"][_class]:
                concreteClasses.append({'name': _class, 'path': f'{globalLookUpDataDict[_class]["absoluteUrlPath"]}'})

        for enum in globalYamlDict["enums"]:
            enumerations.append({'name': enum, 'path': f'{globalLookUpDataDict[enum]["absoluteUrlPath"]}'})

        for _type in globalYamlDict["types"]:
            types.append({'name': _type, 'path': f'{globalLookUpDataDict[_type]["absoluteUrlPath"]}'})
        
        if len(abstractClasses) > 0:
            abstractClasses.sort(key=lambda x: x['name'])
            profile_index_dict['abstractClasses'] = abstractClasses

        if len(concreteClasses) > 0:
            concreteClasses.sort(key=lambda x: x['name'])
            profile_index_dict['concreteClasses'] = concreteClasses

        if len(enumerations) > 0:
            enumerations.sort(key=lambda x: x['name'])
            profile_index_dict['enumerations'] = enumerations

        if len(types) > 0:
            types.sort(key=lambda x: x['name'])
            profile_index_dict['types'] = types

        return profile_index_dict
    
    def mkdocs_create_profile_index():
        path = os.path.join("docs", "Models", "Profiles", globalDocName, "index.md")
        data = mkdocs.mkdocs_profile_index()
        TemplateClass.controller('ProfileOverview.md', data, path, write_file=True)

    def mkdocs_config_handler(config):

        yaml_config_file_path = os.path.join("mkdocs.yaml")

        if config == 'default':
            config = MkDocsConfig.default()
        elif config == 'elbits':
            config = MkDocsConfig.elbits(globalNavDict)

        if os.path.exists('mkdocs.yaml'):
            print("mkdocs.yaml file exists in the root directory.")
            EditMkDocsYaml.controller(yaml_config_file_path, globalNavDict)
        else:
            print("mkdocs.yaml file does not exist in the root directory.")
            TemplateClass.controller("mkdocs.yaml", config, yaml_config_file_path)
            EditMkDocsYaml.controller(yaml_config_file_path, globalNavDict)

    def createNavigationDict():
        navDict = {
            globalDocName: [
                {'Overview': f'Models/Profiles/{globalDocName}/index.md'},
                {"Abstract Classes": []},
                {"Concrete Classes": []},
                {"Enumerations": []},
                {"Types": []}
            ]
        }

        return navDict

class General():
    
    def readYamlSchemaFile(self, yamlSchemaPath):
        with open(yamlSchemaPath, "r") as file: # mkdocs can not take utf-8 but cp1252 , encoding="utf-8"
            
            yamlDict = yaml.safe_load(file)

            return yamlDict

    def includedClasses(self, allClasses=False):
        
        if "attributes" not in globalYamlDict["classes"]["Container"] or globalYamlDict["classes"]["Container"]["attributes"] == None:
            print("Attributes not found in the Container class")
            return
        
        containerClassesSet = set()

        if allClasses == True:
            for _class in globalYamlDict["classes"]:

                if _class == "Container":
                    continue

                containerClassesSet.add(_class)

        if allClasses == False:

            for containerClasses in globalYamlDict["classes"]["Container"]["attributes"]:
                containerClassesSet.add(containerClasses)

        print(len(containerClassesSet), "relevant classes ready for processing")

        return containerClassesSet

    def yamlDictValidation(self):
        print("Validating the yaml file")
        if globalYamlDict == None:
            print("Yaml file is empty")
            return False

        if "classes" not in globalYamlDict or globalYamlDict["classes"] == None:
            print("Classes not found in the yaml file")
            return False
        
        if "prefixes" not in globalYamlDict or globalYamlDict["prefixes"] == None:
            print("Prefixes not found in the yaml file")
            return False
        
        if "Container" not in globalYamlDict["classes"]:
            print("Container class not found in the schema")
            return False
        
        return True

    def createLookUpDict(self):

        lookUpDataDict = {}

        mainUrl = f'/Models/Profiles/{globalDocName}/'
        mainPath = os.path.join("docs", "Models", "Profiles", globalDocName)

        for _class in globalYamlDict['classes']:

            classData = globalYamlDict['classes'][_class]
            abstract = classData['abstract'] if 'abstract' in classData else False

            if abstract == True:
                absoluteUrlPath = f'{mainUrl}AbstractClasses/{_class}/'
                filePath = os.path.join(mainPath, "AbstractClasses" , f"{_class}.md")
                globalNavDict[globalDocName][1]["Abstract Classes"].append({_class: f"Models/Profiles/{globalDocName}/AbstractClasses/{_class}.md"})
            else:
                absoluteUrlPath = f'{mainUrl}ConcreteClasses/{_class}/'
                filePath = os.path.join(mainPath, "ConcreteClasses" , f"{_class}.md")
                globalNavDict[globalDocName][2]["Concrete Classes"].append({_class: f"Models/Profiles/{globalDocName}/ConcreteClasses/{_class}.md"})

            classData = {
                'type': 'class',
                'abstract': abstract,
                'absoluteUrlPath': absoluteUrlPath,
                'filePath': filePath
            }

            lookUpDataDict[_class] = classData

        if 'enums' in globalYamlDict:

            for enumeration in globalYamlDict['enums']:

                abstract = True
                absoluteUrlPath = f'{mainUrl}Enumerations/{enumeration}/'
                filePath = os.path.join(mainPath, "Enumerations" , f"{enumeration}.md")
                globalNavDict[globalDocName][3]["Enumerations"].append({enumeration: f"Models/Profiles/{globalDocName}/Enumerations/{enumeration}.md"})


                enumerationData = {
                    'type': 'enumeration',
                    'abstract': abstract,
                    'absoluteUrlPath': absoluteUrlPath,
                    'filePath': filePath
                }

                lookUpDataDict[enumeration] = enumerationData

        if 'types' in globalYamlDict:

            for _type in globalYamlDict['types']:

                abstract = True
                absoluteUrlPath = f'{mainUrl}Types/{_type}/'
                filePath = os.path.join(mainPath, "Types" , f"{_type}.md")
                globalNavDict[globalDocName][4]["Types"].append({_type: f"Models/Profiles/{globalDocName}/Types/{_type}.md"})

                typeData = {
                    'type': 'type',
                    'abstract': abstract,
                    'absoluteUrlPath': absoluteUrlPath,
                    'filePath': filePath
                }

                lookUpDataDict[_type] = typeData

        return lookUpDataDict

class InheritanceData():

    def getClassInheritance(self, startingClass, _class, inheritanceDict):
        _class = _class

        if _class not in globalYamlDict["classes"] or globalYamlDict["classes"][_class] == None:
            return

        if startingClass not in inheritanceDict:
            
            inheritanceDict[startingClass] = [{startingClass: globalYamlDict["classes"][startingClass]}]

        if "is_a" not in globalYamlDict["classes"][_class] or globalYamlDict["classes"][_class]["is_a"] == None:
            return

        nextClass = globalYamlDict["classes"][_class]["is_a"]

        if nextClass not in globalYamlDict["classes"] or globalYamlDict["classes"][nextClass] == None:
            return

        classData = {nextClass: globalYamlDict["classes"][nextClass]}

        inheritanceDict[startingClass].append(classData)

        InheritanceData().getClassInheritance(startingClass, nextClass, inheritanceDict)

    def getInheritanceClasses(self, _class, inheritanceDict):
        if _class not in inheritanceDict:
            return
        
        keys = [list(d.keys())[0] for d in inheritanceDict[_class]]

        return keys
    
    def getInheritanceDict(self, _class):
        inheritanceDict = {}
        InheritanceData().getClassInheritance(_class, _class, inheritanceDict)
        return inheritanceDict

    def getSubClasses(self, _class):
        _class = _class

        subClassList = []

        for key in globalYamlDict["classes"]:

            if "is_a" not in globalYamlDict["classes"][key] or globalYamlDict["classes"][key]["is_a"] == None:
                continue

            if globalYamlDict["classes"][key]["is_a"] != _class:
                continue

            subClass = key #{key: globalYamlDict["classes"][key]}

            subClassList.append(subClass)

            return subClassList

class ClassData():

    def getEnumData(self):

        if "enums" not in globalYamlDict:
            return

        enumList = []

        for enum in globalYamlDict["enums"]:
            enumName = enum
            enumDescription = globalYamlDict["enums"][enum]["description"] if "description" in globalYamlDict["enums"][enum] else "No description available"
            enum_uri = globalYamlDict["enums"][enum]["enum_uri"] if "enum_uri" in globalYamlDict["enums"][enum] else "No URI available"
            permissible_values = globalYamlDict["enums"][enum]["permissible_values"] if "permissible_values" in globalYamlDict["enums"][enum] else "No permissible values available"

            enumValues = []

            for value in permissible_values:
                
                value = value
                meaning = permissible_values[value]["meaning"] if "meaning" in permissible_values[value] else "No meaning available"
                description = permissible_values[value]["description"] if "description" in permissible_values[value] else "No description available"
                enumValues.append({"enum_uri": f"{enum_uri}.{value}", "value": value, "meaning": meaning, "description": description})

            enumList.append({enumName: {"description": enumDescription, "enum_uri": enum_uri, "permissible_values": enumValues}})

        return enumList
    
    def getTypesData(self):

        if "types" not in globalYamlDict:
            return

        typesList = []

        for _type in globalYamlDict["types"]:
            typeName = _type
            typeDescription = globalYamlDict["types"][_type]["description"] if "description" in globalYamlDict["types"][_type] and globalYamlDict["types"][_type]["description"] != '' else "No description available"
            type_uri = globalYamlDict["types"][_type]["uri"] if "uri" in globalYamlDict["types"][_type] else "No URI available"
            type_annotations = globalYamlDict["types"][_type]["annotations"] if "annotations" in globalYamlDict["types"][_type] else None

            if type_annotations != None:
                type_cim_data_type = globalYamlDict["types"][_type]["annotations"]["cim_data_type"] if "cim_data_type" in globalYamlDict["types"][_type]["annotations"] else False
                type_annotations_uri = globalYamlDict["types"][_type]["annotations"]["uri"] if "uri" in globalYamlDict["types"][_type]["annotations"] else "No URI available"
            else:
                type_cim_data_type = False
                type_annotations_uri = "No URI available"

            typesList.append({typeName: {"description": typeDescription, "uri": type_uri, "cim_data_type": type_cim_data_type, "annotations_uri": type_annotations_uri}})

        return typesList

    def getIndexData(self):
        
        vocabularyDict = {}

        title = globalYamlDict["title"] if "title" in globalYamlDict else "No title available"
        uri = globalYamlDict["id"] if "id" in globalYamlDict else "No URI available"
        name = globalYamlDict["name"] if "name" in globalYamlDict else "No name available"

        vocabularyDict["title"] = title
        vocabularyDict["uri"] = uri
        vocabularyDict["name"] = name

        classList = []
        classListOrdered = []

        for _class in globalYamlDict["classes"]:
            if _class == "Container":
                continue
            classListOrdered.append(_class)

        classListOrdered.sort()

        for _class in classListOrdered:
            description = globalYamlDict["classes"][_class]["description"] if "description" in globalYamlDict["classes"][_class] else "No description available"
            classList.append({_class: description})

        vocabularyDict["Classes"] = classList

        if "enums" not in globalYamlDict:
            return vocabularyDict

        enumList = []
        enumListOrdered = []

        for enum in globalYamlDict["enums"]:
            enumListOrdered.append(enum)

        enumListOrdered.sort()

        for enum in enumListOrdered:
            description = globalYamlDict["enums"][enum]["description"] if "description" in globalYamlDict["enums"][enum] else "No description available"
            enumList.append({enum: description})

        vocabularyDict["Enums"] = enumList

        return vocabularyDict

    def getURL(self, prefix):
        
        prefixes = globalYamlDict["prefixes"]
        
        if prefix not in prefixes or prefixes[prefix] == None:
            return
        
        url = prefixes[prefix]

        return url
        
    def getIs_a(self, _class):

        for key in globalYamlDict["classes"]:
            
            if key != _class:
                continue

            if "is_a" not in globalYamlDict["classes"][key] or globalYamlDict["classes"][key]["is_a"] == None:
                return
            
            return globalYamlDict["classes"][key]["is_a"]

    def getClassNames(self):
        return globalYamlDict["classes"].keys() if "classes" in globalYamlDict else None

    def getCompleteUri(self, classUri):
        prefix = classUri.split(":")[0]

        if prefix not in globalYamlDict["prefixes"] or globalYamlDict["prefixes"][prefix] == None:
            return

        completeUri = globalYamlDict["prefixes"][prefix] + classUri.split(":")[1]
        return completeUri

    def createDataDict(self):
        dataDict = {}

        global globalClass
        globalClass = ""

        for _class in globalYamlDict["classes"]:
            
            globalClass = _class

            if _class not in globalContainerClassesSet:
                continue

            inheritanceDict = InheritanceData().getInheritanceDict(_class)
            classUri = globalYamlDict["classes"][_class]["class_uri"] if "class_uri" in globalYamlDict["classes"][_class] else None
            dataDict[_class] = {}
            dataDict[_class]["title"] = _class
            dataDict[_class]["description"] = globalYamlDict["classes"][_class]["description"] if "description" in globalYamlDict["classes"][_class] else 'No description available'
            dataDict[_class]["abstract"] = globalYamlDict["classes"][_class]["abstract"] if "abstract" in globalYamlDict["classes"][_class] else False
            dataDict[_class]["path"] = globalLookUpDataDict[_class]["filePath"]
            dataDict[_class]["uri"] = classUri if classUri != None else 'No URI available'
            dataDict[_class]["completeUri"] = ClassData().getCompleteUri(classUri) if classUri != None else 'No URI available'
            dataDict[_class]["mermaidString"] = CreateMermaid().createMermaid(inheritanceDict)
            dataDict[_class]["inheritanceString"] = CreateMarkdownFile().createInheritanceString(inheritanceDict)
            dataDict[_class]["tableString"] = CreateMarkdownFile().createAttributeTableString(inheritanceDict) if _class in inheritanceDict else None
            dataDict[_class]["schemaSource"] = globalYamlDict["id"] if "id" in globalYamlDict else "Missing id in Schema"

        return dataDict

class CreateMermaid():

    def createMermaidSubMixinString(self, inheritanceList):
        
        mixinsList = []
        
        for _class in globalYamlDict["classes"]: # For classes that have themselfs as mixins

            if "mixins" not in globalYamlDict["classes"][_class] or globalYamlDict["classes"][_class]["mixins"] == None:
                continue

            mixins = globalYamlDict["classes"][_class]["mixins"]

            if globalClass not in mixins:
                continue

            for mixin in mixins:
                if mixin not in inheritanceList:
                    return

                mixinsList.append({_class: mixin})

        return mixinsList

    def createMermaidMixinsString(self, inheritanceList):
        
        mixinsList = []

        for _class in inheritanceList:

            if "mixins" not in globalYamlDict["classes"][_class] or globalYamlDict["classes"][_class]["mixins"] == None:
                continue

            mixins = globalYamlDict["classes"][_class]["mixins"]
            mixinsList.append({_class: mixins})
        
        if len(mixinsList) == 0:
            return

        return mixinsList
            
    def createMermaidInheritanceString(self, inheritanceList):
        
        inheritanceMermaidList = []
        
        for value in inheritanceList:
            is_a = ClassData().getIs_a(value)
            if value != is_a:
                inheritanceMermaidList.append({value: is_a})

        inheritanceString = ""
        subClassList = []
        for object in inheritanceMermaidList:
            
            for value in object.items():
                subClassList.append(value[1])

            for key, value in object.items():
                if value == None:
                    continue

                inheritanceString += f'''
        {value} <|-- {key} : inherits
            click {value} href "{globalLookUpDataDict[value]["absoluteUrlPath"]}"
            style {value} rx:10,ry:10
'''
                
                if key not in subClassList: # Adding SubClass to the inheritance list
                    inheritanceString += f'''
        {key}
            click {key} href "{globalLookUpDataDict[key]["absoluteUrlPath"]}"
            style {key} rx:10,ry:10
'''
        mixinList = CreateMermaid().createMermaidMixinsString(inheritanceList)

        if mixinList != None:
            for mixin in mixinList:
                for key in mixin:
                    for value in mixin[key]:
                        inheritanceString += f'''
        {value} <|-- {key} : inherits
            click {value} href "{globalLookUpDataDict[value]["absoluteUrlPath"]}"
            style {value} fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10
'''
        
        subMixinList = CreateMermaid().createMermaidSubMixinString(inheritanceList)

        if subMixinList != None:
            for subMixin in subMixinList:
                for key in subMixin:
                    thisClass = subMixin[key]
                    subClass = key
                    inheritanceString += f'''
        {subClass} --|> {thisClass} : inherits
            click {subClass} href "{globalLookUpDataDict[subClass]["absoluteUrlPath"]}"
            style {subClass} fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10
'''

        return inheritanceString

    def createMermaidRelationshipString(self, inheritanceList):

        relationshipString = ""
        classes = globalYamlDict["classes"]

        # From class to range
        for _class in inheritanceList:
            
            if "attributes" not in classes[_class] or classes[_class]["attributes"] == None:
                continue

            for attribute in classes[_class]["attributes"]:

                if "range" not in classes[_class]["attributes"][attribute] or classes[_class]["attributes"][attribute]["range"] == None:
                    continue

                _range = classes[_class]["attributes"][attribute]["range"]
                if _range in classes:

                    relationshipString += f"""        {_class} --> {_range} : {_class}.{attribute}

        {_range}
            click {_range} href "{globalLookUpDataDict[_range]["absoluteUrlPath"]}"
            style {_range} fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10
"""
        # Range to class
        for _class in classes:

            if "attributes" not in classes[_class] or classes[_class]["attributes"] == None:
                continue

            for attribute in classes[_class]["attributes"]:

                if "range" not in classes[_class]["attributes"][attribute] or classes[_class]["attributes"][attribute]["range"] == None:
                    continue

                _range = classes[_class]["attributes"][attribute]["range"]

                if _class == "Container":
                    continue

                if _range in inheritanceList:

                    relationshipString += f"""
        {_class} --> {_range} : {_class}.{attribute}

        {_class}
            click {_class} href "{globalLookUpDataDict[_class]["absoluteUrlPath"]}"
            style {_class} fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10
"""

        return relationshipString

    def createMermaidEnumString(self, inheritanceList):
        
        enumString = ""

        if "enums" not in globalYamlDict:
            return

        enums = globalYamlDict["enums"]

        classes = globalYamlDict["classes"]

        for _class in inheritanceList:
            
            if "attributes" not in classes[_class] or classes[_class]["attributes"] == None:
                continue

            for attribute in classes[_class]["attributes"]:

                if "range" not in classes[_class]["attributes"][attribute] or classes[_class]["attributes"][attribute]["range"] == None:
                    continue

                _range = classes[_class]["attributes"][attribute]["range"]

                if _range in enums:
                    enumString += f'''        {_class} --> {_range} : {_class}.{attribute}

        {_range}
            click {_range} href "{globalLookUpDataDict[_range]["absoluteUrlPath"]}"
            style {_range} fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10
'''
        return enumString

    def createMermaidAttributeString(self, inheritanceList):
        _list = inheritanceList
        _list.reverse()
        attributeString = ""
        for object in _list:
            for key in object:
                if "attributes" not in object[key] or object[key]["attributes"] == None:
                    continue
                attributes = object[key]["attributes"]
                for attribute in attributes:
                    if "slot_uri" not in attributes[attribute] or attributes[attribute]["slot_uri"] == None:
                        continue
                    slot_uri = attributes[attribute]["slot_uri"]
                    attributeString += f'        {key} : {slot_uri.split(":")[1]}\n'
        return attributeString

    def createMermaid(self, inheritanceDict):

        if len(inheritanceDict) == 0:
            return

        inheritanceList = InheritanceData().getInheritanceClasses(globalClass, inheritanceDict)
        totalInheritanceList = inheritanceList

        subClassesList = InheritanceData().getSubClasses(globalClass)

        if subClassesList != None:
            totalInheritanceList = subClassesList + inheritanceList

        inheritanceString = CreateMermaid().createMermaidInheritanceString(totalInheritanceList) if CreateMermaid().createMermaidInheritanceString(totalInheritanceList) != None else ""
        relationshipString = CreateMermaid().createMermaidRelationshipString(inheritanceList) if CreateMermaid().createMermaidRelationshipString(inheritanceList) != None else ""
        enumString = CreateMermaid().createMermaidEnumString(inheritanceList) if CreateMermaid().createMermaidEnumString(inheritanceList) != None else ""
        attributeString = CreateMermaid().createMermaidAttributeString(inheritanceDict[globalClass]) if CreateMermaid().createMermaidAttributeString(inheritanceDict[globalClass]) != None else ""
        mermaidString = f'''
```mermaid
classDiagram
    class {globalClass}
    click {globalClass} href "{globalLookUpDataDict[globalClass]["absoluteUrlPath"]}"
    style {globalClass} fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10
{inheritanceString}
{relationshipString}
{enumString}
{attributeString}```
'''
        
        return mermaidString

class CreateMarkdownFile():

    def createEnums(self):
        
        enumList = ClassData().getEnumData()

        for enum in enumList:
            for key in enum:
                
                description = enum[key]["description"] if "description" in enum[key] else "No description available"
                uri = enum[key]["enum_uri"] if "enum_uri" in enum[key] else "No URI available"
                sourceUri = globalYamlDict["id"].replace('#', '') if "id" in globalYamlDict else "No URI available"

                path = os.path.join("docs", "Models", "Profiles", globalDocName, "Enumerations" , f"{key}.md")
                os.makedirs(os.path.dirname(path), exist_ok=True)

                with open(path, 'w') as file:
                    file.write(f'# {key}\n\n')
                    file.write(f'_{description}_\n\n')
                    file.write(f'**URI**: {uri}\n\n')
                    file.write(f'**Type**: Enumeration\n\n')
                    file.write(f'## Permissible Values\n\n')
                    file.write(f'| Value | Meaning | Description |\n')
                    file.write(f'| --- | --- | --- |\n')

                    for value in enum[key]["permissible_values"]:

                        enumValue = value["value"] if "value" in value else "No value available"
                        meaning = value["meaning"] if "meaning" in value else "No meaning available"
                        enumDescription = value["description"] if "description" in value else "No description available"
                        enum_uri = value["enum_uri"] if "enum_uri" in value else "No URI available"
                        
                        file.write(f'| {enumValue} | [{meaning}]({enum_uri}) | {enumDescription} |\n')

                    file.write(f'## Schema Source\n\n')
                    file.write(f'from schema: [{sourceUri}]({sourceUri})\n')

                print(f'Markdown file created for the enumeration {key}')

    def createTypes(self):

        typesList = ClassData().getTypesData()

        for _type in typesList:
            for key in _type:
                
                description = _type[key]["description"] if "description" in _type[key] else "No description available"
                uri = _type[key]["uri"] if "uri" in _type[key] else "No URI available"
                cim_data_type = _type[key]["cim_data_type"] if "cim_data_type" in _type[key] else False
                annotations_uri = _type[key]["annotations_uri"] if "annotations_uri" in _type[key] else "No URI available"
                sourceUri = globalYamlDict["id"].replace('#', '') if "id" in globalYamlDict else "No URI available"
                
                cim_data_type_text = "This is a CIM data type" if cim_data_type == True else None

                path = os.path.join("docs", "Models", "Profiles", globalDocName, "Types" , f"{key}.md")
                os.makedirs(os.path.dirname(path), exist_ok=True)

                with open(path, 'w') as file:
                    file.write(f'# {key}\n\n')
                    file.write(f'_{description}_\n\n') if description != None else None
                    file.write(f'*{cim_data_type_text}*\n\n') if cim_data_type_text != None else None
                    file.write(f'**URI**: {uri}\n\n')
                    file.write(f'**Type**: Types\n\n')
                    file.write(f'**Annotation URI**: {annotations_uri}\n\n')

                    file.write(f'## Schema Source\n\n')
                    file.write(f'from schema: [{sourceUri}]({sourceUri})\n')

                print(f'Markdown file created for the enumeration {key}')

    def createIndex(self):
        
        vocabularyData = ClassData().getIndexData()

        path = os.path.join("docs", "index.md")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        with open(path, 'w') as file:

            file.write(f'# {vocabularyData["title"]}\n\n')
            file.write(f'**URI**: {vocabularyData["uri"]}\n\n')
            file.write(f'**Name**: {vocabularyData["name"]}\n\n')

            file.write(f'## Classes\n\n')
            file.write(f'| Class | Description |\n')
            file.write(f'| --- | --- |\n')

            for _class in vocabularyData["Classes"]:
                for key, value in _class.items():
                    file.write(f'| [{key}]({key}.md) | {value} |\n')

            file.write(f'\n\n## Enumerations\n\n')

            file.write(f'| Enumeration | Description |\n')
            file.write(f'| --- | --- |\n')

            for enum in vocabularyData["Enums"]:
                for key, value in enum.items():
                    file.write(f'| [{key}]({key}.md) | {value} |\n')

        print('Markdown file created for Index')

    def createAttributeTableString(self, inheritanceDict):
        _list = inheritanceDict[globalClass]
        tableAttribiuteString = ""
        for object in _list:
            for key in object:
                if "attributes" not in object[key] or object[key]["attributes"] == None:
                    continue
                attributes = object[key]["attributes"]
                for attribute in attributes:
                    name = attribute
                    slot_uri = attributes[attribute]["slot_uri"] if "slot_uri" in attributes[attribute] else 'No URI available'
                    prefix = slot_uri.split(":")[0]                    
                    nonPrefix = slot_uri.split(":")[1] if slot_uri != 'No URI available' else 'No URI available'
                    url = ClassData().getURL(prefix)
                    _URI = f'[{slot_uri}]({url}{nonPrefix})' if slot_uri != 'No URI available' else 'No URI available'
                    minimum_cardinality = attributes[attribute]["minimum_cardinality"] if "minimum_cardinality" in attributes[attribute] else None
                    maximum_cardinality = attributes[attribute]["maximum_cardinality"] if "maximum_cardinality" in attributes[attribute] else None

                    rangeList = []

                    if "any_of" in attributes[attribute]:
                        any_of = attributes[attribute]["any_of"]
                        for _dict in any_of:
                            value = _dict["range"]
                            if value in globalYamlDict["classes"]:
                                rangeList.append(f'[{value}]({value}.md)')
                            elif value in globalYamlDict["enums"]:
                                rangeList.append(f'[{value}]({value}.md)')
                            else:
                                rangeList.append(value)
                    elif "range" in attributes[attribute]:
                        rangeList = [attributes[attribute]["range"]]

                    _range = ' or '.join(rangeList)
                    
                    multivalued = attributes[attribute]["multivalued"] if "multivalued" in attributes[attribute] else False
                    maximum_cardinality = "*" if multivalued == True else maximum_cardinality
                    cardinality = f'{minimum_cardinality}..{maximum_cardinality}' if minimum_cardinality != None and maximum_cardinality != None else 'No cardinality available'
                    cardninality_and_range = f'''{cardinality} {_range}'''
                    description = attributes[attribute]["description"] if "description" in attributes[attribute] else 'No description available'
                    inheritance = key if key != globalClass else 'direct'
                    tableAttribiuteString += f'| {name} | {_URI} | {cardninality_and_range} | {description} | {inheritance} |\n'

        return tableAttribiuteString

    def createInheritanceString(self, inheritanceDict):
        if len(inheritanceDict) == 0:
            return
        
        inheritanceList = InheritanceData().getInheritanceClasses(globalClass, inheritanceDict)
        inheritanceList.reverse()
        inheritanceString = '''
## Inheritance
'''
        count = 0
        for key in inheritanceList:
            if key == globalClass:
                inheritanceString += f'{" " * (4 * count)}* **{key}**\n'
            else:
                inheritanceString += f'{" " * (4 * count)}* [{key}]({key}.md)\n'
            count += 1
        return inheritanceString

    def create_markdown_file(self, classDataDict):
        title = classDataDict["title"]
        description = classDataDict["description"]
        abstract = classDataDict["abstract"]
        uri = classDataDict["uri"]
        completeUri = classDataDict["completeUri"]
        schemaSource = classDataDict["schemaSource"].replace('#', '')
        path = classDataDict["path"]

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'w') as file:
            file.write(f"# {title}\n\n")
            file.write(f'_{description}_\n\n')
            file.write(f'*__NOTE__: this is an abstract class and should not be instantiated directly\n\n') if abstract == True else None
            file.write(f'**URI**: [{uri}]({completeUri})<br />\n')
            file.write(f'**Type**: Class\n')
            file.write(f'{classDataDict["mermaidString"]}')
            file.write(f'{classDataDict["inheritanceString"]}\n')
            file.write(f'## Attributes\n')
            file.write(f'| Name | URI | Cardinality and Range | Description | Inheritance |\n')
            file.write(f'| ---  | --- | --- | --- | --- |\n')
            file.write(f'{classDataDict["tableString"]}\n')
            file.write(f'### Schema Source\n')
            file.write(f'* from schema: [{schemaSource}]({schemaSource})\n')

    def create_markdown_files(self):
        dataDict = ClassData().createDataDict()
        for _class in dataDict:

            if _class not in globalContainerClassesSet:
                continue

            CreateMarkdownFile().create_markdown_file(dataDict[_class])

            print(f"Markdown file created for {_class}")

class CreateMdController():

    def main(self, schemaName, template='default'):

        yamlSchemaPath = f"schemas/yaml/{schemaName}.linkml.yaml"
        
        global globalDocName
        globalDocName = ''.join(word.capitalize() for word in schemaName.split('_'))

        global globalYamlDict
        globalYamlDict = General().readYamlSchemaFile(yamlSchemaPath)

        global globalNavDict
        globalNavDict = mkdocs.createNavigationDict()

        global globalLookUpDataDict
        globalLookUpDataDict = General().createLookUpDict()

        global globalContainerClassesSet
        globalContainerClassesSet = General().includedClasses(allClasses=True)

        if General().yamlDictValidation() == False:
            print("Yaml file is not valid")
            exit()
        else:
            print("Yaml file is valid")

        CreateMarkdownFile().createEnums()
        CreateMarkdownFile().createTypes()
        CreateMarkdownFile().create_markdown_files()
        # CreateMarkdownFile().createIndex()

        mkdocs.mkdocs_config_handler(template)
        mkdocs.mkdocs_create_profile_index()

if __name__ == "__main__":
    schemaName = "watt_app"
    CreateMdController().main(schemaName, 'elbits')

