#!/bin/bash

# Get the last commit ID from the current Git repository
git log -n 1 --pretty=format:"%H"
