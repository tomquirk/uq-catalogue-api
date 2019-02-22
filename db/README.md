# UQ Catalogue Web Scraper

## Prerequisites

- Python 3 and [Pipenv](https://github.com/pypa/pipenv)
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

2.2. Create a virtualenv with [Pipenv](https://github.com/pypa/pipenv) (_preferred_):

```bash
$ pipenv install --dev
```

2.3. Activate virtual env

```bash
$ pipenv shell
```

### 3.0 Run the scraper

```
$ python -m src.pipeline
```

Get a coffee, this might take a while...

## The `scrape` Package

The `scrape` package defines all methods for scraping specific parts of the UQ website. It resides under `scrape/`. Example data for which the scrapers are currently configured live in `test/data/*` - respective urls are at the top of these files (commented out)

## Notes and definitions

#### Program

- A degree program e.g Bachelor of Engineering (Honours)
- identifier takes the form of [0-9]{4} (i.e. 2424)

#### Plan

- Generally a major e.g. Software Engineering **plan** (or "major") of the Bachelor of Engineering (Honours) **program**
- identifier takes the form of [A-Z]{6}[0-9]{4} e.g. SOFTWX2002
