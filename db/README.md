# UQ Catalogue Web Scraper

## Prerequisites

- Python 3.x and virtualenv (or [Pipenv](https://github.com/pypa/pipenv))
- PostgreSQL Server

## Installation

### 1.0 Prepare a database

1.1. Create a new database named `uq_catalogue`

1.2. Import the schema from `schema.sql`

```bash
$ psql uq_catalogue < db/schema.sql
```

### 2.0 Set up Python environment

2.1. Create a `.env` file and configure it appropriately. An example is provided - `.env.example`

2.2. Create a virtualenv

```bash
$ virtualenv --python=python3 .venv && source .venv/bin/activate && pip install -r requirements.txt
```

Or with [Pipenv](https://github.com/pypa/pipenv) (*preferred*):

```bash
$ pipenv install
```

2.3. Load the environment variables from the `.env` file (if you're using [Pipenv](https://github.com/pypa/pipenv) , you can skip this step)

### 3.0 Run the scraper

```
$ python pipeline.py
```

Get a coffee, this might take a while...

## The `scrape` Package

The `scrape` package defines all methods for scraping specific parts of the UQ website. It resides under `scrape/`. Example data for which the scrapers are currently configured live in `test/data/*` - respective urls are at the top of these files (commented out)
