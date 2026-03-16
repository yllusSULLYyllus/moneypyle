# !bin/bash

sudo systemctl start docker
docker container start mp-data

source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_SETTINGS_MODULE=config.dev_settings 

python manage.py migrate
python manage.py runserver
