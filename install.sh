#!/bin/bash
# py -m venv venv # If you do not have venv installed. use this the first time
source venv/Scripts/activate
pip install -r requirements.txt
pip install -e .

# Run:
# chmod +x install.sh
# source install.sh