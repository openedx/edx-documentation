#!/bin/bash

# Allows you to preview the HTML for a project "live" in a browser view that updates everytime an ReST file is changed.

[ $# -eq 0 ] && { echo "Usage: $0 path/to/project [port]"; exit 1; }

if [ -z "$(which sphinx-autobuild)" ]
then
    echo "sphinx-autobuild not found. You can install it with the command 'pip install -r shared/tools.txt'. Exiting."
    exit 2
fi

project_dir=$1
port=${2:-9090}

cd $1
make html
sphinx-autobuild -b html -d build/doctrees -c source source build/html --port $port
