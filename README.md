# CIM for Norway CLI Tool

This tool leverages LinkML YAML schemas and YAML data files as input.

## Features

- Generate documentation from schemas and data files
- TBA

# CIM Tool

## Getting Started

### Prerequisites

- Download and install [CIMTool](https://github.com/cimug-org/CIMTool) — CIMug's CIMTool for the Common Information Model (CIM).

### Setup Instructions

1. **Clone the repository**
2. **Create a new branch**  
    Example: `feature/outage_owl_improvements`
3. **Create a new CIMTool Project**
    - Set any project name you prefer
    - Do not include any copyrights
    - Set your preferences as needed
    - For the Intial Schema Import, browse to `<ThisRepository>/models/` and select the `.eap` file
    - Click **Finish** to create an empty CIMTool project
4. **Add an OWL file to your project**
    - Go to `New > General > File`
    - Select the parent folder: `<YourProjectName>/Profiles`
    - Click **Advanced >>**
    - Choose to link to a file in the file system
    - Browse to `<ThisRepository>/schemas/owl/<TheFileYouWant>.owl`
    - Click **Finish**
5. **Edit the OWL file**  
    You can now edit the `.owl` file as needed; changes will be reflected in your branch by using normal git operations.
6. **Working with other files**  
    If you need to create or edit other files (e.g., `.linkml`), remember that all files are based on the `.owl` file. If you update the `.owl` file, manually copy the updated `.linkml` (or other formats) into the correct folder in the repository.

> **Tip:** Keep your branch up to date with the latest changes from the main branch to avoid conflicts.