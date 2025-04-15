import os

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
    pass


def split_by_region(countries: list[Country], directory: str):
    regions = group_by_region(countries)
    os.makedirs("regions", exist_ok=True)
    for key, value in regions.items:
        file_path = os.path.join(directory, f"{key}.csv")
        write_to_file(value, file_path)