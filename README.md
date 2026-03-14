# Moneypyle

This is a simple double-entry bookkeeping app. This is meant to be no frills. The basics are solid. The work goes into making little modules that create useful functionality

## Dev Setup
### Project setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Set up env variables:

`cp .env.example .env`

Fill out with the correct variables for your app
### Database container setup

Look over the `docker-compose.dev.yml`. This 
#### on *most* linux:

`systemctl start docker`

#### on MacOS
  Just start the docker daemon.

`docker compose -f docker-compose.dev.yml up -d`
## Running the dev evironment
### First time run
After running the database setup, you container should be running. To start the dev server and finish configuring the database:
```
export DJANGO_SETTINGS_MODULE=config.dev_settings
python manage.py migrate
python manage.py runserver
```
### Run an already-setup project
```
docker container start mp-data
export DJANGO_SETTINGS_MODULE=config.dev_settings
python manage.py runserver
```
## Deploying Project
working on it