import yaml

class InputAdapterYamlSchema:
    
    def readYamlSchemaFile(yamlSchemaPath):
        with open(yamlSchemaPath, "r") as file:
            
            yamlDict = yaml.safe_load(file)

            if 'classes' in yamlDict:
                if 'Container' in yamlDict['classes']:
                    yamlDict['classes'].pop('Container')

            return yamlDict
        
class Controller:

    def main(schemaName):
        yamlSchemaPath = f"schemas/yaml/{schemaName}.linkml.yaml"
        dict = InputAdapterYamlSchema.readYamlSchemaFile(yamlSchemaPath)
        return dict

if __name__ == "__main__":
    schemaName = "aviation_obstacle"
    print(Controller.main(schemaName))