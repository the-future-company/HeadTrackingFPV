#!/bin/bash

# Navigate to your project directory
PROJECT_DIR="$HOME/HeadTrackingFPVRaspberryPi"
PYTHON_SCRIPT="src.wifi_direct_setup.wifi_direct_manager"
ALIAS_NAME="setup_wifi_direct_connection"

# Check if the alias exists in ~/.bash_aliases
if ! grep -q "alias $ALIAS_NAME=" ~/.bash_aliases; then
    echo "Adding alias '$ALIAS_NAME' to ~/.bash_aliases"
    # Add an alias that uses 'pipenv run'
    echo "alias $ALIAS_NAME='cd $PROJECT_DIR && pipenv install && pipenv run python -m $PYTHON_SCRIPT'" >> ~/.bash_aliases
    # Apply the changes to the current environment
    source "$HOME/.bashrc"
else
    echo "Alias $ALIAS_NAME already exists."
fi
