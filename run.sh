#!/bin/bash

cd src
if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    python3 -m venv .venv
    source .venv/bin/activate
fi

pip install graphviz bcrypt tk
python3 page_control.py