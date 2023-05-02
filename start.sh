#!/bin/bash

while true
do
 gunicorn -c ./GCB_Django/conf/guniconf-config.py GCB_Django.wsgi
done
