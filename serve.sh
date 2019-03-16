#!/bin/sh

./build.py

cd public
python -m http.server

