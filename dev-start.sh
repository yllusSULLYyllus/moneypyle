# !bin/bash

sudo systemctl start docker # If on Mac, comment this out. Starting the Docker Daemon does the same thing
docker compose -f docker-compose.dev.yml up -d

source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_SETTINGS_MODULE=config.dev_settings 

python manage.py migrate
python manage.py runserver
