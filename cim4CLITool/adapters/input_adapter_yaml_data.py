import yaml

class InputAdapterYamlData:
    
    def readYamlDataFile(yamlDataPath):
        with open(yamlDataPath, "r") as file:
            
            yamlDict = yaml.safe_load(file)

            return yamlDict
        
class Controller:

    def main(dataName):
        yamlDataPath = f"data/yaml/{dataName}.yaml"
        dict = InputAdapterYamlData.readYamlDataFile(yamlDataPath)
        return dict

if __name__ == "__main__":
    dataName = "aviation_obstacle"
    print(Controller.main(dataName))