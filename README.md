# Python CSV Parsing

This project contains two Python scripts for parsing CSV files:

1. `lab_3.py`: Splits country data by region and writes to individual CSV files.
2. `tests/test_lab_3.py`: Unit tests for `lab_3.py`.

## Setup

1. Clone the repository

```bash
git clone https://github.com/williamagh/python-csv-parsing.git
cd python-csv-parsing
```

2. Install dependencies using uv (for pytest currently)

```bash
uv sync
```

3. Run the script

```bash
python lab_3.py
```

4. Run the test

```bash
uv run pytest tests/test_lab_3.py -v -s
```

## Notes

- The test is currently configured to run against the `csv/input/country_full.csv` file and output to the `tests/test_output/regions` directory.
- The test checks that the number of rows in the output files matches the number of rows in the source file.
- The test checks that the output files are valid CSV files.

## Example Output

```bash
williamcallahan@williams python-csv-parsing % uv run pytest
=============================================================== test session starts ================================================================
platform darwin -- Python 3.12.8, pytest-8.3.5, pluggy-1.5.0
rootdir: /Users/williamcallahan/Developer/git/pycharm/python-csv-parsing
configfile: pyproject.toml
collected 1 item                                                                                                                                   

tests/test_lab_3.py .                                                                                                                        [100%]

================================================================ 1 passed in 0.00s =================================================================
williamcallahan@williams python-csv-parsing % uv run pytest -v -s
=============================================================== test session starts ================================================================
platform darwin -- Python 3.12.8, pytest-8.3.5, pluggy-1.5.0 -- /Users/williamcallahan/Developer/git/pycharm/python-csv-parsing/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/williamcallahan/Developer/git/pycharm/python-csv-parsing
configfile: pyproject.toml
collected 1 item                                                                                                                                   

tests/test_lab_3.py::test_row_count_matches File: Americas.csv, Rows: 57
File: Other.csv, Rows: 1
File: Europe.csv, Rows: 51
File: Oceania.csv, Rows: 29
File: Asia.csv, Rows: 51
File: Africa.csv, Rows: 60
Source rows: 249, Output rows: 249
PASSED

================================================================ 1 passed in 0.01s =================================================================
williamcallahan@williams python-csv-parsing % 
```

