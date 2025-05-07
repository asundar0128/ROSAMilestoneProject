#!/bin/bash

DEFAULT_MODEL="llama4"
echo "Enter model type [llama4/claude/gpt4o] (default: $DEFAULT_MODEL): "
read MODEL_TYPE
export MODEL_TYPE=${MODEL_TYPE:-$DEFAULT_MODEL}

cd "$(dirname "$0")"
source venv/bin/activate
python3 main.py
