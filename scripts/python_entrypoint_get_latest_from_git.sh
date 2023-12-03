#!/bin/bash

# Navigate to your project directory
PROJECT_DIR="$HOME/HeadTrackingFPVRaspberryPi"
PYTHON_SCRIPT="src/raspberry_pi_governer_scripts/get_latest_from_git.py"
ALIAS_NAME="get_latest_from_git"

# Construct the full path to the Python script
PYTHON_SCRIPT_PATH="$PROJECT_DIR/$PYTHON_SCRIPT"

# Check if the alias exists in ~/.bash_aliases
if ! grep -q "alias $ALIAS_NAME=" ~/.bash_aliases; then
    echo "Adding alias to ~/.bash_aliases"
    # Add an alias that uses 'pipenv run'
    echo "alias $ALIAS_NAME='cd $PROJECT_DIR && pipenv run python $PYTHON_SCRIPT_PATH'" >> ~/.bash_aliases
    # Apply the changes to the current environment
    source "$HOME/.bashrc"
else
    echo "Alias $ALIAS_NAME already exists."
fi
