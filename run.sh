#!/bin/bash

cd src

# setup python virtual env
if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    python3 -m venv .venv
    source .venv/bin/activate
fi

# create database if it doesnt exist
if [ ! -f "automata.db" ]; then
    python3 db_setup.py
fi

pip install graphviz bcrypt tk
python3 gui.py