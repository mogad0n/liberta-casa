#!/bin/sh

oragono mkcerts
oragono initdb
oragono run &

python3 flaskapp.py
