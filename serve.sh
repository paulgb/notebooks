#!/bin/sh

set -e

./build.py

cd public
python -m http.server

