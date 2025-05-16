import xmltodict
import re
import os

class General:

    @staticmethod
    def readFile(inputFilePath):
        with open(inputFilePath, "r") as file:
            return file.read()

    @staticmethod
    def writeFile(outputFilePath, xmlData):
        with open(outputFilePath, "w") as file:
            file.write(xmlData)

class XmlSorting:

    @staticmethod
    def writeDictIntoXml(outputFilePath, dictData):
        with open(outputFilePath, "w") as file:
            xmltodict.unparse(dictData, output=file, pretty=True)

    @staticmethod
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

    @staticmethod
    def sortDict(xmlDict):
        xmlDictSorted1 = dict(sorted(xmlDict["rdf:RDF"].items()))
        xmlDict["rdf:RDF"] = xmlDictSorted1
        xmlDictSorted = XmlSorting.sortDictWithPriority(xmlDict)
        return xmlDictSorted

class XmlFormatting:

    @staticmethod
    def formatXmlString(xmlString):
        
        formatted_xml = xmlString.replace("xmlns:", "\n\txmlns:")
        formatted_xml = "\n".join(
            line if not line.startswith("\t</") else f"{line}\n"
            for line in formatted_xml.splitlines()
        )
        formatted_xml = formatted_xml.replace(">\n\t<md:FullModel", "\n\t>\n\n\t<md:FullModel")

        return formatted_xml

    @staticmethod
    def self_closing_tag(xmlString):
        # Replace self-closing tags with a newline
        formatted_xml = re.sub(r'rdf:resource="([^"]*)"></[^>]*>', r'rdf:resource="\1"/>', xmlString)
        return formatted_xml

class ControllerXmlSorting:

    @staticmethod
    def sort_single_files(inputFilePath, outputFilePath, print_output=False, cim4_formatting=False):

        # Read the XML file into a dictionary
        xml_dict = xmltodict.parse(General.readFile(inputFilePath))

        # Sort the dictionary with priority on all levels
        xml_dict_sorted = XmlSorting.sortDict(xml_dict)

        # Convert the sorted dictionary back to XML string with pretty formatting
        xmlString = xmltodict.unparse(xml_dict_sorted, pretty=True)

        if cim4_formatting == True:
            # Apply specific formatting for CIM4

            # Format the XML string for better readability
            output_xml = XmlFormatting.formatXmlString(xmlString)

        else:
            output_xml = xmlString

        # Apply self-closing tag formatting
        output_xml = XmlFormatting.self_closing_tag(output_xml)

        # Write the formatted XML string to the output file
        General.writeFile(outputFilePath, output_xml)

        # Optionally print the formatted XML string
        if print_output:
            print(output_xml)

    @staticmethod
    def sort_multiple_files(input_folder_path, output_folder_path, print_output=False, cim4_formatting=False):
        # List all XML files in the input directory
        xml_files = [f for f in os.listdir(input_folder_path) if f.endswith('.xml')]

        for xml_file in xml_files:
            input_path = os.path.join(input_folder_path, xml_file)
            os.makedirs(output_folder_path, exist_ok=True)
            output_path = os.path.join(output_folder_path, f"sorted_{xml_file}")
            ControllerXmlSorting.sort_single_files(input_path, output_path, print_output, cim4_formatting)

if __name__ == "__main__":
    # Example usage
    # inputFilePath = "data/xml/Telemark-120-LV1_GL.xml"  # Replace with your XML file path
    # outputFilePath = "data/xml/Telemark-120-LV1_GL_sorted.xml"  # Replace with your desired output file path

    # ControllerXmlSorting.main(inputFilePath, outputFilePath, print_output=True, cim4_formatting=True)

    input_folder_path = "data/xml/"  # Replace with your XML file path
    output_folder_path = "data/xml/something_sorted"  # Replace with your desired output file path

    # List all XML files in the input directory
    ControllerXmlSorting.sort_multiple_files(input_folder_path, output_folder_path, print_output=False, cim4_formatting=False)
