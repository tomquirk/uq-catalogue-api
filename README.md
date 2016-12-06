# UQ API (unofficial)
> (Unofficial) API and webscraper for University of Queensland Course and Program Data


## Overview
This project includes the tools to build the MySql database (web scraper and sql schema) as well as the Web API (currently in Node). 


## Getting Started


### Prerequisites
- Node (latest)
- Python 3.x
- MySql Server


### Installation

#### DB/scraper
1. Create a MySql db named `uq_catalogue` with no pwd and import `uq_catalogue_schema.sql`
2. Setup your virtualenv, source it and `cd db`
3. `pip install -r requirements.txt`
4. `python3 scrape.py` and enter your db details
5. Get a coffee, this might take a while...

#### API
1. In the root dir, `npm install`
2. `npm start`


## Contributing
Always open for PRs! Try to make an issue before submitting a PR to increase transparency.
