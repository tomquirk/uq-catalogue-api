# UQ Catalogue Web Scraper

## Prerequisites

- Python 3.x and virtualenv
- PostgreSQL Server

## Installation

To build the database:

1. Create a PostgreSQL db (something like `uq_catalogue`) and import schema from `schema.sql`

```bash
psql uq_catalogue < db/schema.sql
```

2. Setup your virtualenv using python3 and install dependencies

```bash
virtualenv --python=python3 .venv && source .venv/bin/activate && pip install -r requirements.txt
```

4. Run `python pipeline.py` and enter your db details

5. Get a coffee, this might take a while...

## Scrape Package

The Scrape package defines all methods for scraping specific parts of the UQ website. It resides under `scrape/`.
