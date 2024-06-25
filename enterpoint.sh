#!/bin/bash
export PATH="/home/cmake-3.18.0-Linux-x86_64/bin:/usr/local/gcc-8.2/bin:${PATH}"

gunicorn --workers 1 --bind 0.0.0.0:8000 app:app