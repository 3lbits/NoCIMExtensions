.PHONY: markdown
markdown: ## Generate Markdown files from LinkML schemas and removes all Slot and Type files
	gen-doc -d docs/AviationObstacle --diagram-type mermaid_class_diagram --template-directory _templates/ --use-slot-uris schemas/aviationobstacle.linkml.yaml
	grep -E '^# (Slot|Type): ' -lr --include \*.md docs | xargs -d '\n' rm

startup_powershell:
	venv/Scripts/activate

startup_bash:
	source venv/Scripts/activate

ao:
	linkml-convert -s AO_schema.yaml AO.yaml -t ttl -o AO.ttl
	linkml-convert -s AO_schema.yaml AO.yaml -t json-ld -o AO.jsonld
	linkml-convert -s AO_schema.yaml AO.yaml -t json -o AO.json
	linkml-convert -s AO_schema.yaml AO.yaml -t rdf -o AO.rdf

all:
	make clean
	make markdown
	python python/replace_star_with_0dotdotstar.py
	mkdocs serve

.PHONY: protobuf
protobuf: ## Generate Protobuf files from LinkML schemas
	mkdir -p protobufs
	gen-proto schemas/aviationobstacle.linkml.yaml > protobufs/aviationobstacle.proto

.PHONY: python
python: ## Generate Python dataclass files from LinkML schemas
	mkdir -p python
	gen-python schemas/aviationobstacle.linkml.yaml > python/aviationobstacle.py

.PHONY: clean
clean: ## Delete all Markdown files
	rm docs/AviationObstacle/*.md

########################## Next section: Made by Thomas #################################

# Default parameter if none is provided
yamlDataFilePath ?= data/yaml/aviationobstacle.yaml
yamlSchemaFilePath ?= schemas/aviationobstacle.linkml.yaml
outputFilePath ?= data/jsonld/aviationobstacle.jsonld
outputFilePathLinkMl ?= data/jsonld/aviationobstacle_linkml.jsonld
string1 ?= nc-no
string2 ?= ncno

# Rule to run the linkml-convert command with a parameter
.PHONY: linkmljsonld help

# LinkML conversion target with HELP=1 check
linkmljsonld:
	@if [ "$(help)" = "1" ]; then \
		echo "Usage: make linkmljsonld yamlSchemaFilePath=<Your yaml Schema File Path> yamlDataFilePath=<Your yaml Data File Path> outputFilePathLinkMl=<Your Output File Path>"; \
	else \
		python python/replace_oldstring_with_newstring.py $(yamlSchemaFilePath) $(string1) $(string2); \
		linkml-convert -s $(yamlSchemaFilePath) $(yamlDataFilePath) -t json-ld -o $(outputFilePathLinkMl); \
		python python/replace_oldstring_with_newstring.py $(yamlSchemaFilePath) $(string2) $(string1); \
	fi

# Example: make linkmljsonld yamlSchemaFilePath=schemas/aviationobstacle.linkml.yaml yamlDataFilePath=data/yaml/aviationobstacle.yaml outputFilePath=data/jsonld/aviationobstacle.linkml.jsonld
# Clean linkml command: linkml-convert -s test_AO_schema.yaml test_AO.yaml -t json-ld -o test_AO_linkml.jsonld

# Rule to run the jsonld-convert command with a parameter
.PHONY: jsonld

# JSON-LD conversion target with help check
jsonld:
	@if [ "$(help)" = "1" ]; then \
		echo "Usage: make jsonld yamlSchemaFilePath=<Your yaml Schema File Path> yamlDataFilePath=<Your yaml data File Path> outputFilePath=<Your Output File Path>"; \
	else \
		python python/jsonldFromYamlConverter.py $(yamlSchemaFilePath) $(yamlDataFilePath) $(outputFilePath); \
	fi

# Example1: make jsonld yamlSchemaFilePath=schemas/aviationobstacle.linkml.yaml yamlDataFilePath=data/yaml/aviationobstacle.yaml outputFilePath=data/jsonld/aviationobstacle.jsonld
# Example2: make jsonld yamlSchemaFilePath=schemas/wattapp.linkml.yaml yamlDataFilePath=data/yaml/wattapp.yaml outputFilePath=data/jsonld/wattapp.jsonld

###########################################################
##@ Help
.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)