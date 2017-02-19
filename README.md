# UQ API (unofficial)
> (Unofficial) webscraper and API for University of Queensland Course and Program Data

## Overview
This project includes the tools to build the PostgreSQL database (web scraper and sql schema) as well as the REST API (currently in Node). 

## Getting Started

### Prerequisites
- Node (latest)
- Python 3.x and virtualenv (try pipenv)
- PostgreSQL Server


### Installation

#### DB/scraper
1. Create a PostgreSQL db and import schema from `schema.sql`.
2. In the `db` directory, setup your virtualenv in python3 - `virtualenv --python=python3 .venv && source .venv/bin/activate`
3. Install dependencies - `pip install -p`
4. `python migrations.py` and enter your db details
5. Get a coffee, this might take a while...

#### API
The REST API will depend on an installation of the DB (anywhere).

1. In the root dir, `npm install`
2. `npm start`
3. Defaults to port `3000` - to test, try hitting `localhost:3000/api/course/csse1001`


## Contributing
Always open for PRs! Check the TODOS and try to make an Issue before submitting a PR to increase transparency.

## TODO
- API docs
