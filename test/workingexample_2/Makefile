# Default parameter if none is provided
yamlDataFilePath ?= AO.yaml
yamlSchemaFilePath ?= AO_schema.yaml
outputFilePath ?= AO_created_from_code.jsonld

# Rule to run the linkml-convert command with a parameter
.PHONY: linkmljsonld help

# LinkML conversion target with HELP=1 check
linkmljsonld:
	@if [ "$(help)" = "1" ]; then \
		echo "Usage: make linkmljsonld yamlSchemaFilePath=<Your yaml Schema File Path> yamlDataFilePath=<Your yaml Data File Path> outputFilePath=<Your Output File Path>"; \
	else \
		linkml-convert -s $(yamlSchemaFilePath) $(yamlDataFilePath) -t json-ld -o $(outputFilePath); \
		python jsonldtransformer.py $(outputFilePath) $(yamlSchemaFilePath); \
	fi

# Rule to run the jsonld-convert command with a parameter
.PHONY: jsonld

# JSON-LD conversion target with help check
jsonld:
	@if [ "$(help)" = "1" ]; then \
		echo "Usage: make jsonld yamlSchemaFilePath=<Your yaml Schema File Path> yamlDataFilePath=<Your yaml data File Path> outputFilePath=<Your Output File Path>"; \
	else \
		python jsonldFromYamlConverter.py $(yamlSchemaFilePath) $(yamlDataFilePath) $(outputFilePath); \
	fi

# Usage instructions
help:
	@echo "commands:"
	@echo "make linkmljsonld"
	@echo "make jsonld"
	@echo "--------------------------"
	@echo "For each commands own help instruction you can type make <command> help=1"
