#!/bin/bash
# Ensure PACKY_PATH is defined in the script
export PACKY_PATH="!root-project-path!/packy/packy.py"

echo "Running: python3 $PACKY_PATH -t"
python3 $PACKY_PATH -t
