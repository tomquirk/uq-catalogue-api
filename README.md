# UQ API (unofficial)
> (Unofficial) API and webscraper for University of Queensland Course and Program Data


## Overview
This project includes the tools to build the MySql database (web scraper and sql schema) as well as the Web API (currently in Node). 


## Getting Started


### Prerequisites
- Node (latest)
- Python 3.x and virtualenv
- MySql Server


### Installation

#### DB/scraper
1. Create a MySql db named `uq_catalogue` as root user with no pwd (or change config in `migrations.py` desired) and import `uq_catalogue_schema.sql`
2. Setup your virtualenv in python3 - `virtualenv --python=python3 env`- source it and `cd db`
3. `pip install -r requirements.txt`
4. `python3 migrations.py` and enter your db details
5. Get a coffee, this might take a while...

#### API
1. In the root dir, `npm install`
2. `npm start`
3. Defaults to port `3000` - to test, try hitting `localhost:3000/api/course/csse1001`


## Contributing
Always open for PRs! Check the TODOS and try to make an Issue before submitting a PR to increase transparency.

## TODO
- API docs
- rm lodash
- diff webscraped data for DB migration 
