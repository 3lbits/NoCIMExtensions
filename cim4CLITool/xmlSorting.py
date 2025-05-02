import xmltodict
import json

class General:

    def readFile(inputFilePath):
        with open(inputFilePath, "r") as file:
            return file.read()

    def writeFile(outputFilePath, xmlData):
        with open(outputFilePath, "w") as file:
            file.write(xmlData)

class XmlSorting:

    def writeDictIntoXml(outputFilePath, dictData):
        with open(outputFilePath, "w") as file:
            xmltodict.unparse(dictData, output=file, pretty=True)

    def sortDictWithPriority(d, priority_keys=("@xmlns", "md:FullModel")):
        if isinstance(d, dict):
            # Separate keys based on priority
            priority_items = {k: v for k, v in d.items() if any(k.startswith(pk) for pk in priority_keys)}
            other_items = {k: v for k, v in d.items() if not any(k.startswith(pk) for pk in priority_keys)}
            
            # Sort other items alphabetically
            sorted_other_items = sorted(other_items.items())
            
            # Recursively sort both priority and other items
            sorted_dict = {k: XmlSorting.sortDictWithPriority(v, priority_keys) for k, v in priority_items.items()}
            sorted_dict.update({k: XmlSorting.sortDictWithPriority(v, priority_keys) for k, v in sorted_other_items})
            
            return sorted_dict
        elif isinstance(d, list):
            return [XmlSorting.sortDictWithPriority(i, priority_keys) for i in d]
        else:
            return d

    def sortDict(xmlDict):
        xmlDictSorted1 = dict(sorted(xmlDict["rdf:RDF"].items()))
        xmlDict["rdf:RDF"] = xmlDictSorted1
        xmlDictSorted = XmlSorting.sortDictWithPriority(xmlDict)
        return xmlDictSorted

class XmlFormatting:

    def formatXmlString(xmlString):
        
        formatted_xml = xmlString.replace("xmlns:", "\n\txmlns:")
        formatted_xml = "\n".join(
            line if not line.startswith("\t</") else f"{line}\n"
            for line in formatted_xml.splitlines()
        )
        formatted_xml = formatted_xml.replace(">\n\t<md:FullModel", "\n\t>\n\n\t<md:FullModel")

        return formatted_xml

class ControllerXmlSorting:

    def main(inputFilePath, outputFilePath, print_output=False):

        # Read the XML file into a dictionary
        xml_dict = xmltodict.parse(General.readFile(inputFilePath))

        # Sort the dictionary with priority on all levels
        xml_dict_sorted = XmlSorting.sortDict(xml_dict)

        # Convert the sorted dictionary back to XML string with pretty formatting
        xmlString = xmltodict.unparse(xml_dict_sorted, pretty=True)

        # Format the XML string for better readability
        formatted_xml = XmlFormatting.formatXmlString(xmlString)

        # Write the formatted XML string to the output file
        General.writeFile(outputFilePath, formatted_xml)

        # Optionally print the formatted XML string
        if print_output:
            print(formatted_xml)

if __name__ == "__main__":
    # Example usage
    inputFilePath = "data/xml/Telemark-120-LV1_GL.xml"  # Replace with your XML file path
    outputFilePath = "data/xml/Telemark-120-LV1_GL_sorted.xml"  # Replace with your desired output file path

    ControllerXmlSorting.main(inputFilePath, outputFilePath, print_output=True)