#!/bin/sh
oragono mkcerts
oragono initdb
oragono run &
cd /app/kiwi && yarn run dev && 
cd /app
mkdir -vp /run/nginx/
nginx -c /etc/nginx/conf.d/default.conf
python3 flaskapp.py
