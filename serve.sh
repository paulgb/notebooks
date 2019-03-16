#!/bin/sh

./convert_notebooks.py

cd public
python -m http.server

