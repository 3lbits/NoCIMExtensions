import yaml

class General():
    
    def readYamlSchemaFile(self, yamlSchemaPath):
        with open(yamlSchemaPath, "r") as file:
            global yamlDict
            yamlDict = yaml.safe_load(file)

    def includedClasses(self, allClasses=False):
        
        if "attributes" not in yamlDict["classes"]["Container"] or yamlDict["classes"]["Container"]["attributes"] == None:
            print("Attributes not found in the Container class")
            return
        
        global containerClassesSet
        containerClassesSet = set()

        if allClasses == True:
            for _class in yamlDict["classes"]:

                if _class == "Container":
                    continue

                containerClassesSet.add(_class)

        if allClasses == False:

            for containerClasses in yamlDict["classes"]["Container"]["attributes"]:
                containerClassesSet.add(containerClasses)

        print(len(containerClassesSet), "relevant classes ready for processing")

        # containerClassesSet = {"CableInfo"}
        # print("Using only CableIngfo class for now")

    def yamlDictValidation(self):
        print("Validating the yaml file")
        if yamlDict == None:
            print("Yaml file is empty")
            return False

        if "classes" not in yamlDict or yamlDict["classes"] == None:
            print("Classes not found in the yaml file")
            return False
        
        if "prefixes" not in yamlDict or yamlDict["prefixes"] == None:
            print("Prefixes not found in the yaml file")
            return False
        
        if "Container" not in yamlDict["classes"]:
            print("Container class not found in the schema")
            return False
        
        return True

class InheritanceData():

    def getClassInheritance(self, startingClass, _class, inheritanceDict):
        _class = _class

        if _class not in yamlDict["classes"] or yamlDict["classes"][_class] == None:
            return

        if startingClass not in inheritanceDict:
            
            inheritanceDict[startingClass] = [{startingClass: yamlDict["classes"][startingClass]}]

        if "is_a" not in yamlDict["classes"][_class] or yamlDict["classes"][_class]["is_a"] == None:
            return

        nextClass = yamlDict["classes"][_class]["is_a"]

        if nextClass not in yamlDict["classes"] or yamlDict["classes"][nextClass] == None:
            return

        classData = {nextClass: yamlDict["classes"][nextClass]}

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

        for key in yamlDict["classes"]:

            if "is_a" not in yamlDict["classes"][key] or yamlDict["classes"][key]["is_a"] == None:
                continue

            if yamlDict["classes"][key]["is_a"] != _class:
                continue

            subClass = key #{key: yamlDict["classes"][key]}

            subClassList.append(subClass)

            return subClassList

class ClassData():

    def getEnumData(self):

        if "enums" not in yamlDict:
            return

        enumList = []

        for enum in yamlDict["enums"]:
            enumName = enum
            enumDescription = yamlDict["enums"][enum]["description"] if "description" in yamlDict["enums"][enum] else "No description available"
            enum_uri = yamlDict["enums"][enum]["enum_uri"] if "enum_uri" in yamlDict["enums"][enum] else "No URI available"
            permissible_values = yamlDict["enums"][enum]["permissible_values"] if "permissible_values" in yamlDict["enums"][enum] else "No permissible values available"

            enumValues = []

            for value in permissible_values:
                
                value = value
                meaning = permissible_values[value]["meaning"] if "meaning" in permissible_values[value] else "No meaning available"
                description = permissible_values[value]["description"] if "description" in permissible_values[value] else "No description available"
                enumValues.append({"enum_uri": f"{enum_uri}.{value}", "value": value, "meaning": meaning, "description": description})

            enumList.append({enumName: {"description": enumDescription, "enum_uri": enum_uri, "permissible_values": enumValues}})

        return enumList
    
    def getIndexData(self):
        
        vocabularyDict = {}

        title = yamlDict["title"] if "title" in yamlDict else "No title available"
        uri = yamlDict["id"] if "id" in yamlDict else "No URI available"
        name = yamlDict["name"] if "name" in yamlDict else "No name available"

        vocabularyDict["title"] = title
        vocabularyDict["uri"] = uri
        vocabularyDict["name"] = name

        classList = []
        classListOrdered = []

        for _class in yamlDict["classes"]:
            if _class == "Container":
                continue
            classListOrdered.append(_class)

        classListOrdered.sort()

        for _class in classListOrdered:
            description = yamlDict["classes"][_class]["description"] if "description" in yamlDict["classes"][_class] else "No description available"
            classList.append({_class: description})

        vocabularyDict["Classes"] = classList

        if "enums" not in yamlDict:
            return vocabularyDict

        enumList = []
        enumListOrdered = []

        for enum in yamlDict["enums"]:
            enumListOrdered.append(enum)

        enumListOrdered.sort()

        for enum in enumListOrdered:
            description = yamlDict["enums"][enum]["description"] if "description" in yamlDict["enums"][enum] else "No description available"
            enumList.append({enum: description})

        vocabularyDict["Enums"] = enumList

        return vocabularyDict

    def getURL(self, prefix):
        
        prefixes = yamlDict["prefixes"]
        
        if prefix not in prefixes or prefixes[prefix] == None:
            return
        
        url = prefixes[prefix]

        return url
        
    def getIs_a(self, _class):

        for key in yamlDict["classes"]:
            
            if key != _class:
                continue

            if "is_a" not in yamlDict["classes"][key] or yamlDict["classes"][key]["is_a"] == None:
                return
            
            return yamlDict["classes"][key]["is_a"]

    def getClassNames(self):
        return yamlDict["classes"].keys() if "classes" in yamlDict else None

    def getCompleteUri(self, classUri):
        prefix = classUri.split(":")[0]

        if prefix not in yamlDict["prefixes"] or yamlDict["prefixes"][prefix] == None:
            return

        completeUri = yamlDict["prefixes"][prefix] + classUri.split(":")[1]
        return completeUri

    def createDataDict(self):
        dataDict = {}

        global globalClass

        globalClass = ""

        for _class in yamlDict["classes"]:
            
            globalClass = _class

            if _class not in containerClassesSet:
                continue

            inheritanceDict = InheritanceData().getInheritanceDict(_class)
            classUri = yamlDict["classes"][_class]["class_uri"] if "class_uri" in yamlDict["classes"][_class] else None
            dataDict[_class] = {}
            dataDict[_class]["title"] = _class
            dataDict[_class]["description"] = yamlDict["classes"][_class]["description"] if "description" in yamlDict["classes"][_class] else 'No description available'
            dataDict[_class]["abstract"] = yamlDict["classes"][_class]["abstract"] if "abstract" in yamlDict["classes"][_class] else False
            dataDict[_class]["uri"] = classUri if classUri != None else 'No URI available'
            dataDict[_class]["completeUri"] = ClassData().getCompleteUri(classUri) if classUri != None else 'No URI available'
            dataDict[_class]["mermaidString"] = CreateMermaid().createMermaid(inheritanceDict)
            dataDict[_class]["inheritanceString"] = CreateMarkdownFile().createInheritanceString(inheritanceDict)
            dataDict[_class]["tableString"] = CreateMarkdownFile().createAttributeTableString(inheritanceDict) if _class in inheritanceDict else None
            dataDict[_class]["schemaSource"] = yamlDict["id"] if "id" in yamlDict else "Missing id in Schema"
        return dataDict

class CreateMermaid():

    def createMermaidSubMixinString(self, inheritanceList):
        
        mixinsList = []
        
        for _class in yamlDict["classes"]: # For classes that have themselfs as mixins

            if "mixins" not in yamlDict["classes"][_class] or yamlDict["classes"][_class]["mixins"] == None:
                continue

            mixins = yamlDict["classes"][_class]["mixins"]

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

            if "mixins" not in yamlDict["classes"][_class] or yamlDict["classes"][_class]["mixins"] == None:
                continue

            mixins = yamlDict["classes"][_class]["mixins"]
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
            click {value} href "../{value}"
            style {value} rx:10,ry:10
'''
                
                if key not in subClassList: # Adding SubClass to the inheritance list
                    inheritanceString += f'''
        {key}
            click {key} href "../{key}"
            style {key} rx:10,ry:10
'''
        mixinList = CreateMermaid().createMermaidMixinsString(inheritanceList)

        if mixinList != None:
            for mixin in mixinList:
                for key in mixin:
                    for value in mixin[key]:
                        inheritanceString += f'''
        {value} <|-- {key} : inherits
            click {value} href "../{value}"
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
            click {subClass} href "../{subClass}"
            style {subClass} fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10
'''

        return inheritanceString

    def createMermaidRelationshipString(self, inheritanceList):

        relationshipString = ""
        classes = yamlDict["classes"]

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
            click {_range} href "../{_range}"
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
            click {_class} href "../{_class}"
            style {_class} fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10
"""

        return relationshipString

    def createMermaidEnumString(self, inheritanceList):
        
        enumString = ""

        if "enums" not in yamlDict:
            return

        enums = yamlDict["enums"]

        classes = yamlDict["classes"]

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
            click {_range} href "../{_range}"
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
    click {globalClass} href "../{globalClass}"
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
                sourceUri = yamlDict["id"].replace('#', '') if "id" in yamlDict else "No URI available"

                with open(f'{docFilePath}{key}.md', 'w') as file:
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

    def createIndex(self):
        
        vocabularyData = ClassData().getIndexData()
        
        with open(f'{docFilePath}index.md', 'w') as file:

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
                            if value in yamlDict["classes"]:
                                rangeList.append(f'[{value}]({value}.md)')
                            elif value in yamlDict["enums"]:
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
        with open(f'{docFilePath}{title}.md', 'w') as file:
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

            if _class not in containerClassesSet:
                continue

            CreateMarkdownFile().create_markdown_file(dataDict[_class])

            print(f"Markdown file created for {_class}")

class Controller():

    def main(self, schemaName):

        yamlSchemaPath = f"schemas/yaml/{schemaName}.linkml.yaml"
        docName = ''.join(word.capitalize() for word in schemaName.split('_'))

        global docFilePath
        docFilePath = f"docs/{docName}/"

        General().readYamlSchemaFile(yamlSchemaPath) # Setting the yamlDict variable globally

        if General().yamlDictValidation() == False:
            print("Yaml file is not valid")
            exit()
        else:
            print("Yaml file is valid")

        General().includedClasses(allClasses=True) # Setting the containerClassesSet variable globally - Using only classes defined in Container class

        CreateMarkdownFile().create_markdown_files()
        CreateMarkdownFile().createIndex()
        CreateMarkdownFile().createEnums()

if __name__ == "__main__":
    schemaName = "watt_app"
    Controller().main(schemaName)
