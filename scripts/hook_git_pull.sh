#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
echo "Script directory: $SCRIPT_DIR"

# Navigate to the script directory
cd "$SCRIPT_DIR" || exit

# Discard any unstaged changes
echo "Discarding all unstaged changes."
git reset --hard

# Pull the latest changes from the master branch
echo "Pulling the latest changes from master."
git fetch origin
git reset --hard origin/master

# Check if the alias exists in ~/.bashrc
if ! grep -q "alias pull_from_git=" ~/.bashrc; then
    echo "Adding alias to ~/.bashrc"
    echo "alias pull_from_git='bash $SCRIPT_DIR/git_pull_script.sh'" >> ~/.bashrc
    # shellcheck disable=SC1090
    source ~/.bashrc
else
    echo "Alias already exists."
fi
