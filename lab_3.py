# CIS-117 Lab 3
# Reads the CSV file containing information on countries and splits the countries by region generating one file per region
# Group# 3 William Callahan - reading part, Vasilisa Zaitseva - writting part

import os
import csv
from typing import List, Dict

class Country:
    """Classifies a country with its name and region."""
    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region

def read_countries(csv_file: str) -> List[Country]:
    """
    Read countries from CSV file and return a list of Country objects
    
    Args:
        csv_file: Path to the CSV file containing country data
        
    Returns:
        List of Country objects
    """
    countries: List[Country] = []
    try:
        with open(csv_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                # Assign "Other" as region for entries with empty region
                region = row['region'] if row['region'] else "Other"
                countries.append(Country(row['name'], region))
    except (IOError, FileNotFoundError, PermissionError) as e:
        print(f"Error reading from {csv_file}: {e}")
    return countries

def group_by_region(countries: list[Country]) -> Dict[str, List[Country]]:
    """
    Group countries by their region
    
    Args:
        countries: List of Country objects
        
    Returns:
        Dictionary mapping region names to lists of countries
    """
    region_dict: Dict[str, List[Country]] = {}
    for country in countries:
        region_dict.setdefault(country.region, []).append(country)
    return region_dict

def write_to_file(countries: list[Country], file_name: str):
    """
    Write a list of countries to a CSV file
    
    Args:
        countries: List of Country objects to write
        file_name: Path to the output file
    """
    try:
        with open(file_name, 'w') as f:
            f.write("Name,Region\n")
            for country in countries:
                f.write(f"{country.name},{country.region}\n")
    except (IOError, FileNotFoundError, PermissionError) as e:
        print(f"Error writing to {file_name}: {e}")

def split_by_region(countries: list[Country], directory: str):
    """
    Split countries by region and write each region to a separate CSV file
    
    Args:
        countries: List of Country objects
        directory: Directory to store the output files
    """
    regions = group_by_region(countries)
    os.makedirs(directory, exist_ok=True)
    for key, value in regions.items():
        file_path = os.path.join(directory, f"{key}.csv")
        write_to_file(value, file_path)

if __name__ == "__main__":
    input_file = "country_full.csv"
    output_dir = "regions"
    
    print(f"Reading countries from {input_file}...")
    countries = read_countries(input_file)
    
    if countries:
        print(f"Found {len(countries)} countries.")
        print(f"Splitting countries by region into directory: {output_dir}")
        split_by_region(countries, output_dir)
        print("Process completed.")
    else:
        print("No countries found or error reading the file.")