#!/bin/bash
source venv/Scripts/activate
pip install -r requirements.txt
pip install -e .

# Run:
# chmod +x install.sh
# source install.sh