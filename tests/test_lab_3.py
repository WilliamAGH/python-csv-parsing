import pytest
import os
import csv
import shutil
import sys

# Importing lab_3 to test
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lab_3 import read_countries, split_by_region

def count_csv_rows(file_path):
    """Count the number of rows in a CSV file, excluding the header"""
    with open(file_path, 'r') as f:
        return sum(1 for _ in csv.reader(f)) - 1  # Subtract 1 for header

def test_row_count_matches():
    """Test that the sum of rows in output files matches the source file"""
    # Input and output paths
    input_file = "csv/input/country_full.csv"  # Path relative to project root
    output_dir = "tests/test_output/regions"
    
    # Clean up any existing test output directory
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    # Count rows in source file
    source_rows = count_csv_rows(input_file)
    
    # Process the data
    countries = read_countries(input_file)
    split_by_region(countries, output_dir)
    
    # Count rows in all output files
    total_output_rows = 0
    output_files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
    
    for output_file in output_files:
        file_path = os.path.join(output_dir, output_file)
        rows = count_csv_rows(file_path)
        total_output_rows += rows
        print(f"File: {output_file}, Rows: {rows}")
    
    # Assert that the counts match
    print(f"Source rows: {source_rows}, Output rows: {total_output_rows}")
    assert total_output_rows == source_rows, f"Row count mismatch: source={source_rows}, output={total_output_rows}"
    
    # Clean up
    shutil.rmtree(output_dir) 