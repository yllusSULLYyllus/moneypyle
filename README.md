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
There is also a scrit
The app should be running at `localhost:8000/moneypyle`

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

## Deploying Project
working on it