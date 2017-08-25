# UQ Catalogue Web Scraper

## Prerequisites

- Python 3.x and virtualenv
- PostgreSQL Server

## Installation

To build the database:

1. Create a PostgreSQL db (something like `uq_catalogue`) and import schema from `schema.sql`
1. In the `db` directory, setup your virtualenv using python3

```bash
virtualenv --python=python3 .venv && source .venv/bin/activate
```

1. Install dependencies - `pip install -r requirements.txt`
1. `python migrations.py` and enter your db details
1. Get a coffee, this might take a while...
