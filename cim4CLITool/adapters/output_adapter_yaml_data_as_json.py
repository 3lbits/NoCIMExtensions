from cim4CLITool.adapters.input_adapter_yaml_data import InputAdapterYamlData
from cim4CLITool.domain.data_model import DataModel
import json
from dacite import from_dict  # helps with nested dataclasses

class Controller:

    @staticmethod
    def run(filpath):
        # Input Adapter: read from YAML file
        data_dict = InputAdapterYamlData.readYamlDataFile(filpath)

        # Model: create internal dataclass
        dataSet = from_dict(data_class=DataModel, data=data_dict)

        # Output Adapter: convert to JSON, including nested dataclasses
        output_json = json.dumps(dataSet, default=lambda o: o.__dict__, indent=4)

        print(output_json)

if __name__ == "__main__":
    filpath = "data/yaml/aviation_obstacle.yaml"
    Controller.run(filpath)