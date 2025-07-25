# Job Comparison Tool

🛠️ A Python-based tool that compares job definitions across environments (DEV, UAT, PROD) to identify discrepancies.

## Features:
- Compares JSON-formatted job definitions
- Outputs side-by-side differences
- Used to streamline QA and reduce mismatches in production jobs

## Technologies:
Python, JSON, CLI

## Usage:
1. Place job files (e.g., `dev_jobs.json`, `prod_jobs.json`) in the root folder  
2. Run: `python compare_jobs.py`
3. View output highlighting missing or mismatched job configs
