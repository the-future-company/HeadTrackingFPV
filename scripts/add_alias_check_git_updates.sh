#!/bin/bash

# The path to the Python script
PYTHON_SCRIPT_PATH="/path/to/your/python_script.py"

# The desired alias name
ALIAS_NAME="check_git_updates"

# Check if the alias exists in ~/.bashrc
if ! grep -q "alias $ALIAS_NAME=" ~/.bashrc; then
    echo "Adding alias to ~/.bashrc"
    echo "alias $ALIAS_NAME='python3 $PYTHON_SCRIPT_PATH'" >> ~/.bashrc
else
    echo "Alias already exists."
fi
