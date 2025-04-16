# CIS-117 Lab3
# Reads the CSV file containing information on countries and splits the countries by region generating one file per region
# Group# 3 William Callahan - reading part, Vasilisa Zaitseva - writting part

import os
from typing import List, Dict

class Country:
    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region

def group_by_region(countries: list[Country]) -> Dict[str, List[Country]]:
    region_dict: Dict[str, List[Country]] = {}
    for country in countries:
        region_dict.setdefault(country.region, []).append(country)
    return region_dict

def write_to_file(countries: list[Country], file_name: str):
    try:
        with open(file_name, 'w') as f:
            f.write("Name,Region\n")
            for country in countries:
                f.write(f"{country.name},{country.region}\n")
    except (IOError, FileNotFoundError, PermissionError) as e:
        print(f"Error writing to {file_name}: {e}")

def split_by_region(countries: list[Country], directory: str):
    regions = group_by_region(countries)
    os.makedirs(directory, exist_ok=True)
    for key, value in regions.items():
        file_path = os.path.join(directory, f"{key}.csv")
        write_to_file(value, file_path)