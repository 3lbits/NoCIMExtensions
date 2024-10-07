# CIM4NoUtility Profile Documentation
This repo contains LinkML artifacts and documentation for the Common Power System Model (CPSM) and CPSM Network Analysis (NA) profile groups. CPSM and CPSM-NA are two foundational Common Information Model (CIM) profile groups that define the classes, class attributes, and associations from the CIM required to model transmission network models and represent solved state estimation or power flow results.

## To Use this

### Make commands

- ```make all```

  - This recreates the documentation based on the yaml schema files using these commands

  - ```make clean```
  - ```make markdown```
  - ```python python/replace_star_with_0dotdotstar.py```
  - ```mkdocs serve```

- ```make linkmljsonld```

  - This is using linkml to create jsonld based on yaml schema and yaml data files

  - ```python python/replace_oldstring_with_newstring.py $(yamlSchemaFilePath) $(string1) $(string2); \```
  - ```linkml-convert -s $(yamlSchemaFilePath) $(yamlDataFilePath) -t json-ld -o $(outputFilePathLinkMl); \```
  - ```python python/replace_oldstring_with_newstring.py $(yamlSchemaFilePath) $(string2) $(string1); \```

- ```make jsonld```
  
  - This is using python to create jsonld based on yaml schema and yaml data files

  - ```python python/jsonldFromYamlConverter.py $(yamlSchemaFilePath) $(yamlDataFilePath) $(outputFilePath); \```

  - Example: ```make jsonld yamlSchemaFilePath=schemas/aviationobstacle.linkml.yaml yamlDataFilePath=data/yaml/aviationobstacle.yaml outputFilePath=data/jsonld/aviationobstacle.jsonld```


## Contributing
To run the site locally use [Python](https://www.python.org/) 3.11+. It will likely be easiest to use a Python virtual environment as shown below to install the dependencies.
```cmd
python -m venv venv
venv\Scripts\activate
pip install mkdocs-material linkml
```
For exact (known working) versions of dependencies, run `pip install -r requirements.txt` instead.

Once installed, you can then run the documentation site locally with hot reload using `mkdocs serve`
```cmd
mkdocs serve
```
Or you can build the static HTML files once with
```sh
mkdocs build
```

### Updating or adding schemas
This project uses [LinkML](https://linkml.io/) to generate Markdown files from LinkML schemas. So a typical workflow for working on this project is to add or update LinkML `.yaml` files to the `schemas` subdirectory, do the following:

1. Run the `make clean` command to delete all Markdown files in the subdirectories of `docs`. It does not change `images` and `stylesheets` subdirectories or the `docs/index.md` file.
```sh
make clean
```
2. Use [LinkML's Markdown generator](https://linkml.io/linkml/generators/markdown.html) to create the static Markdown files from the LinkML schema by running `make markdown`
```sh
make mardown
```

This is using `Makefile` to hide the complexity of running commands manually. You can see the full usage by running `make help`.

Note that if a new profile has been added, make sure to add it to the list in the `docs/index.md` file.


# LinkML commands

- linkml-convert -s personinfo.linkml.yaml data.linkml.yaml -o data.jsonld