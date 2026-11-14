# CSV Cleaner

A small Python tool that cleans a CSV file by trimming extra spaces and removing completely blank or duplicate rows.

## Features

- Reads `input.csv`
- Trims spaces around cell values
- Skips blank rows
- Removes exact duplicate rows
- Saves the result as `cleaned.csv`

## How to run

Place `input.csv` in the project folder, then run:

```bash
python cleaner.py