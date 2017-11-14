# Logparsers

This repository contains a collection of parsers and utilities for managing semi-structured log files.

## Introduction

Logparsers is an extensible framework for parsing semi-structured unix logfiles into a structure typesafe form suitable for loading into spreadsheets or databases.

Implementations currently exist for the following formats:

-   Apache
-   Nginx
-   Postfix
-   Auth

## Installation

Make sure that the cloned directory is in your `PYTHONPATH`. For example mine is in `~/lib/python/logparsers`.

To use the utilities you can symlink the contents of the `bin` directory to a directory in your `PATH`:

```bash
# my home bin dir is in PATH
cd bin
ln -s ../lib/python/logparsers/bin/logexporter.py logexporter
```

## Usage

Usage is simple. To find out the options type

```bash
logexporter -h
usage: logexporter [-h] [-f FORMAT] [-o OUTPUT] [-v] FILENAMES [FILENAMES ...]

Exports logfiles to CSV.

positional arguments:
  FILENAMES             List of input files

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Inputfile format; one of auth, postfix, nginx, apache
  -o OUTPUT, --out OUTPUT
                        The file where the unparseable lines should be written
                        (default: write to stdout)
  -v, --verbose         output parse errors
```

For example to convert an apache logfile `access.log` into a tab delimited file you would type:

```bash
logexporter -f apache -o access.tsv access.log
```

## Testing

All parsers have a test suite and related features. To run cd into the logparsers directory and type:

```bash
python -m logparsers/tests/[parser name]_test.py
```
Where [parser name] is one of the available parsers.

## Requirements

1. Python 3.5+
