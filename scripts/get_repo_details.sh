#!/bin/bash

# Extracts the owner and repository name from the remote URL
REMOTE_URL=$(git remote get-url origin)

# Check for HTTPS remote URL
if [[ $REMOTE_URL =~ https:// ]]; then
    OWNER_REPO=$(echo "$REMOTE_URL" | sed -e 's/https:\/\/github.com\///;s/.git$//')
else
    # Assume SSH format
    OWNER_REPO=$(echo "$REMOTE_URL" | sed -e 's/git@github.com://;s/.git$//')
fi

echo "$OWNER_REPO"
