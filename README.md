# Data Processing and CI Workflow

This project includes scripts for processing data from an Excel file, converting it to CSV, and running a Python script to analyze the data. It also contains GitHub Actions workflow configuration to automate testing with ruff, executing the script, and deploying results.

## Files

- `execute.py`: Python script that reads data.xlsx, processes data, and outputs analysis results in JSON.
- `data.csv`: CSV version of `data.xlsx`.
- `.github/workflows/ci.yml`: GitHub Actions workflow configuration.

## How to run

1. Ensure you're using Python 3.11+ and Pandas 2.3 installed.
2. Run `python execute.py` to generate `result.json`.
3. Serve `index.html` via a static server or open directly in a browser to view results.

## CI Workflow

The workflow automates linting with ruff, execution of `execute.py`, and publishes `result.json` via GitHub Pages.

## Notes

- Make sure to push the code with `data.csv`, `execute.py`, and the `.github/workflows/ci.yml` as configured.
- The `result.json` is generated dynamically in CI and not committed.