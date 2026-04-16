# Sample Time App

A small terminal app that shows the current local time and date and updates every second.

## Set up dev tools

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Run the app

```bash
python3 -m sample_time_app
```

## Run the linter

```bash
.venv/bin/python -m ruff check .
```

## Run the tests

```bash
.venv/bin/python -m pytest
```
