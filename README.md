# Moneypyle

This is a simple double-entry bookkeeping app. This is meant to be no frills. The basics are solid. The work goes into making little modules that create useful functionality. It's an opportunity to get familiar with django

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

Look over the `docker-compose.dev.yml`. This creates a volume in docker and attaches it to a container.
#### on *most* linux:

`systemctl start docker`

#### on MacOS
  Just start the docker daemon.

Then run

`docker compose -f docker-compose.dev.yml up -d`

By default this creates a conytainer named `mp-data` and a volume named `moneypyle_pgdata`

To check if the volume was made and the container is running run:
```
docker ps
docker volume ls
```

Your output will be similar to:
``` 
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                                         NAMES
a77e8d6ba0a9   postgres:latest   "docker-entrypoint.s…"   14 minutes ago   Up 14 minutes   0.0.0.0:6543->5432/tcp, [::]:6543->5432/tcp   mp-data
DRIVER    VOLUME NAME
local     moneypyle_pgdata
```

Make sure the names in the `NAME` columns are what you expect. If so, you should be good to continue
## Running the dev evironment
### First time run
After running the database setup, the container should be running. To start the dev server and finish configuring the database:
```
export DJANGO_SETTINGS_MODULE=config.dev_settings
python manage.py migrate
python manage.py runserver
```
### Run an already-setup project
```
docker compose -f docker-compose.dev.yml up -d
export DJANGO_SETTINGS_MODULE=config.dev_settings
python manage.py runserver
```
There is also a script called `/dev-start.sh` that runs this whole process. Adjust to your needs. 

After doing `chmod +x dev-start.sh` You will be able to run the script using 

`./dev-start.sh`

The app should be running at `localhost:8000/moneypyle`
### Cleanly Wrapping Up
just use: 
`docker compose down` 

and close out the webserver in your terminal with ctrl+c

## Usage
| Note: in dev, the basse URL will be `localhost:8000/moneypyle`
### Sitemap
### Endpoints
#### Accounts
---
By its use in everyday speach, we might think that an account is simply a bank account; something that you store and draw money from. In accounting, though, an account is just a category. Yes, it is your Bank Account, but it could also be the accrued value of Fuel over time. Funcitonally, an account is used to represent *types* of value that are changing within the accounting system (i.e. your business) over a certain period of time. That is what is meant here by `account`

---

`/accounts`

`/accounts/<id>`

  endpoint to GET information about a single account

#### Transactions
---
Transactions are simple to understand, since we make them everyday. You use money from your bank account to buy some tacos from a tacos truck. In accounting, this would be represented as a decrease in value in your Bank Account, and an increase in value of your Meals account. 

This helps to highlight the major point of accounting: it is a tracking system!

---
`/journal`
POST accept a new transaction

#### Party
---
In `moneypyle`, all entities are considered a party. There is no distinction between a customer or vendor. Even a Company is considered a party in these terms. Think of it like a restaurant: "MP, party of four!"

`/party`
GETs all parties in the database.

---
## Primer on Accounting Language and Concepts
### Accounts
By its use in everyday speach, we might think that an account is simply a bank account; something that you store and draw money from. In accounting, though, an account is just a category. Yes, it is your Bank Account, but it could also be the accrued value of Fuel over time. Funcitonally, an account is used to represent *types* of value that are changing within the accounting system (i.e. your business) over a certain period of time. That is what is meant here by `account`
#### Default Accounts

#### Big 5 Types
Assets
Liabilities
Equity
Income/Revenue
Expenses
#### There are really only 3
Assets
Liabilities
Equity = (Owner Contributions) + (Income - Expenses) 
### Transactions
There are more complex examples that can help to show why it's important think of these events as changes in *value* rather than an increase and decrease in money.

All other types of transactions are just an abstraction of this basic idea.
### The Accounting Formula
Assets = Liabilities + Equity
#### Different Conceptualizations of THis

A = what you own

L = what you owe

E = owner's slice of the pie

---

## Todos

- make transaction pages for certain transaction types
  - deposits (bank account)
  - invoices (AR)
  - bills (AP)
- make user authentication
  - make pages login only
  - make calls with auth token
  - define RLS
- create categroization staging area
  - bulk uploads happen here
- improve links
- improve endpoint names
- 
- (longterm) incorporate AJAX
- 


## Deploying Project
working on it