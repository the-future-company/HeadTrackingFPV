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
git reset --hard origin/main
