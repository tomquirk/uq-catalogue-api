# UQ Catalogue API (unofficial)

:mortar_board: (Unofficial) webscraper and API for University of Queensland Course and Program Data

## Overview

This project includes the tools to build the PostgreSQL database (web scraper and sql schema) as well as the REST API (currently in Node).

## Getting Started

### Prerequisites
- Node (latest)
- Python 3.x and virtualenv
- PostgreSQL Server

## Installation

### Build Database

1. Create a PostgreSQL db (something like `uq_catalogue`) and import schema from `schema.sql`
1. In the `db` directory, setup your virtualenv using python3

```bash
virtualenv --python=python3 .venv && source .venv/bin/activate
```

1. Install dependencies - `pip install -r requirements.txt`
1. `python migrations.py` and enter your db details
1. Get a coffee, this might take a while...

#### API

The REST API will depend on an installation of the DB. By default, it looks for `localhost:5432/uq_catalogue`.

1. In the root dir, `npm install`
1. `npm start`
1. Defaults to port `3000` - to test, try hitting `localhost:3000/api/course/csse1001`

## Contributing

Always open for PRs! Check the TODOS and try to make an Issue before submitting a PR to increase transparency.
