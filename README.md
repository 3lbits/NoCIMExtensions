# CIM4 CLI Tool

A command-line tool for working with CIM (Common Information Model) extensions for Norway's power grid. It uses [LinkML](https://linkml.io/) YAML schemas and YAML data files as input to generate documentation, convert data formats, and sort XML files.

## Features

- **Documentation generation** — Generate Markdown documentation from LinkML YAML schemas, served locally with MkDocs Material
- **YAML to JSON-LD conversion** — Convert YAML data files to JSON-LD using a LinkML schema
- **JSON Schema generation** — Create JSON Schema from LinkML YAML schemas
- **XML sorting** — Sort CIM/XML files (single or bulk) with optional CIM4-specific formatting
- **Schema tools** — Migrate CIM datatype classes from `classes:` to `types:` section in LinkML schemas
- **UUID generation** — Generate one or more UUIDv4 values

## Getting Started

### Prerequisites

- Python 3.10+

### Setup (PowerShell)

```powershell
.\startup.ps1
```

This creates a virtual environment, installs dependencies, and installs the `cim4` CLI in editable mode.

### Manual Setup

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
# .\venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
pip install -e .
```

## Usage

After setup, the `cim4` command is available in the activated virtual environment.

```
cim4 --help
```

### Generate Documentation

```bash
# Generate docs for a specific schema
cim4 docs gen -s aviation_obstacle

# Serve docs locally
mkdocs serve
```

### Convert YAML to JSON-LD

```bash
# Using a common file name (schema, data, and output share the same name)
cim4 jsonld gen -f aviation_obstacle

# Using explicit paths
cim4 jsonld gen -s aviation_obstacle -d aviation_obstacle -o aviation_obstacle
```

### Generate JSON Schema

```bash
cim4 json schema -s aviation_obstacle
```

### Sort XML Files

```bash
# Sort a single file by name (looks in data/xml/)
cim4 xml sort -f Telemark-120-LV1_GL

# Sort with explicit input/output paths
cim4 xml sort -i path/to/input.xml -o path/to/output.xml

# Bulk sort all XML files in a folder
cim4 xml sort -b -i path/to/folder -o path/to/output_folder

# With CIM4 formatting
cim4 xml sort -f Telemark-120-LV1_GL -c
```

### Generate UUIDs

```bash
cim4 uuidv4         # Generate 1 UUID
cim4 uuidv4 -n 5    # Generate 5 UUIDs
```

### Migrate CIM Datatype Classes

Auto-detects CIM datatype classes (classes with only `value`/`unit`/`multiplier` attributes) and moves them from `classes:` to the `types:` section.

```bash
# Preview what would be migrated across all schemas
cim4 schema migrate-datatypes --dry-run

# Migrate all schemas
cim4 schema migrate-datatypes

# Migrate a single schema
cim4 schema migrate-datatypes -s core_equipment
```

## Project Structure

```
schemas/yaml/       LinkML YAML schema definitions
data/yaml/          YAML instance data
data/jsonld/        Generated JSON-LD output
data/xml/           XML files (input/output for sorting)
schemas/json/       Generated JSON Schemas
docs/               Generated MkDocs documentation source
cim4CLITool/        CLI tool source code
```

## Acknowledgements

The CGMES (Common Grid Model Exchange Standard) LinkML schemas used in this project are sourced from [Netbeheer-Nederland/cgmes](https://github.com/Netbeheer-Nederland/cgmes) — ENTSO-E CGMES profiles represented as LinkML schemas. The Norwegian extension profiles are maintained by us.

## Before you start