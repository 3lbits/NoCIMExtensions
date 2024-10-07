# Default parameter if none is provided
yamlDataFilePath ?= AO.yaml
yamlSchemaFilePath ?= AO_schema.yaml
outputFilePath ?= AO.jsonld
outputFilePathLinkMl ?= AO_linkml.jsonld
string1 ?= nc-no
string2 ?= ncno

# Rule to run the linkml-convert command with a parameter
.PHONY: linkmljsonld help

# LinkML conversion target with HELP=1 check
linkmljsonld:
	@if [ "$(help)" = "1" ]; then \
		echo "Usage: make linkmljsonld yamlSchemaFilePath=<Your yaml Schema File Path> yamlDataFilePath=<Your yaml Data File Path> outputFilePathLinkMl=<Your Output File Path>"; \
	else \
		python replace_oldstring_with_newstring.py $(yamlSchemaFilePath) $(string1) $(string2); \
		linkml-convert -s $(yamlSchemaFilePath) $(yamlDataFilePath) -t json-ld -o $(outputFilePathLinkMl); \
		python replace_oldstring_with_newstring.py $(yamlSchemaFilePath) $(string2) $(string1); \
	fi

# Example: make linkmljsonld yamlSchemaFilePath=AO_schema.yaml yamlDataFilePath=AO.yaml outputFilePathLinkMl=AO_linkml.jsonld
# Clean linkml command: linkml-convert -s test_AO_schema.yaml test_AO.yaml -t json-ld -o test_AO_linkml.jsonld

# Rule to run the jsonld-convert command with a parameter
.PHONY: jsonld

# JSON-LD conversion target with help check
jsonld:
	@if [ "$(help)" = "1" ]; then \
		echo "Usage: make jsonld yamlSchemaFilePath=<Your yaml Schema File Path> yamlDataFilePath=<Your yaml data File Path> outputFilePath=<Your Output File Path>"; \
	else \
		python jsonldFromYamlConverter.py $(yamlSchemaFilePath) $(yamlDataFilePath) $(outputFilePath); \
	fi

# Example: make jsonld yamlSchemaFilePath=AO_schema.yaml yamlDataFilePath=AO.yaml outputFilePath=AO.jsonld

# Usage instructions
help:
	@echo "commands:"
	@echo "make linkmljsonld"
	@echo "make jsonld"
	@echo "--------------------------"
	@echo "For each commands own help instruction you can type make <command> help=1"
