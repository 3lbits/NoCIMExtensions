.PHONY: markdown
markdown: ## Generate Markdown files from LinkML schemas and removes all Slot and Type files
	gen-doc -d docs/AviationObstacle --diagram-type mermaid_class_diagram --template-directory _templates/ --use-slot-uris schemas/aviationobstacle.linkml.yaml
	grep -E '^# (Slot|Type): ' -lr --include \*.md docs | xargs -d '\n' rm

#powershell: venv/Scripts/activate
#git bash: source venv/Scripts/activate
all:
	make clean
	make markdown
	python replace_star_with_0dotdotstar.py
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

###########################################################
##@ Help
.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)