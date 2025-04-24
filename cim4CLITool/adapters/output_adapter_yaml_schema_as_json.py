from cim4CLITool.adapters.input_adapter_yaml_schema import InputAdapterYamlSchema
from cim4CLITool.domain.schema_model import Vocabulary
import json
from dacite import from_dict  # helps with nested dataclasses

class Controller:

    @staticmethod
    def run():
        # Input Adapter: read from YAML file
        data_dict = InputAdapterYamlSchema.readYamlSchemaFile(
            "schemas/yaml/aviation_obstacle.linkml.yaml"
        )

        # Model: create internal dataclass
        vocab = from_dict(data_class=Vocabulary, data=data_dict)

        # Output Adapter: convert to JSON, including nested dataclasses
        output_json = json.dumps(vocab, default=lambda o: o.__dict__, indent=4)

        print(output_json)

if __name__ == "__main__":
    Controller.run()