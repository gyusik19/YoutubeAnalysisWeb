#!/usr/bin/env bash
set -x
service ssh start

bash ./script/run_migration.sh
#bash ./script/run_django.sh 0 8000
bash ./script/run_gunicorn.sh 0 8080