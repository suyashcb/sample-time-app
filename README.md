# Sample Time App

A small terminal app that shows the current local time and date and updates every second.

## Set up dev tools

```bash
cd /Users/suyash/sample-time-app
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Run the app

```bash
cd /Users/suyash/sample-time-app
python3 -m sample_time_app
```

## Run the linter

```bash
cd /Users/suyash/sample-time-app
.venv/bin/python -m ruff check .
```

## Run the tests

```bash
cd /Users/suyash/sample-time-app
.venv/bin/python -m pytest
```
