import pprint

import pandas as pd
import requests

GDP_INDICATOR = "NY.GDP.MKTP.CD"
GDP_PER_CAPITA_INDICATOR = ""


def run(indicator: str) -> pd.DataFrame:
    athletes = load_athletes_data()
    country_codes = set(athletes['noc'])
    indicator_data: list[dict] = []
    print(f'Going to request {indicator} for {len(country_codes)} countries')
    for country in country_codes:
        start_year = athletes[athletes['noc'] == country]['year'].min()
        end_year = athletes[athletes['noc'] == country]['year'].max()
        try:
            getIndicatorForCountry(indicator, country, start_year, end_year, indicator_data)
        except Exception as error:
            print(f'Error getting indicator for country {country}')
            print(error)

    df = pd.DataFrame(indicator_data)
    return df



def getIndicatorForCountry(indicator: str, country_code: str, start_year: int, end_year: int, indicator_data: list[dict]):

    has_nex_page = True
    page = 1

    while has_nex_page:
        has_nex_page = process_request(indicator, country_code, start_year, end_year, page, indicator_data)
        page += 1



def process_request(indicator: str, country_code: str, start_year: int, end_year: int, page: int, indicator_data: list[dict]) -> bool:
    has_next_page = False
    gdp_url = f"https://api.worldbank.org/v2/country/{country_code}/indicators/{indicator}"
    print(f'Sending request for {country_code} page {page}')
    response = requests.get(gdp_url, params={
        "date": f"{start_year}:{end_year}",
        "format": "json",
        "page": page
    })
    if response.status_code == 200:
        response_data = response.json()

        if len(response_data) != 2:
            print(f'Unexpected response')
            pprint.pprint(response_data)
            return has_next_page

        pagination_data = response_data[0]
        if pagination_data['page'] < pagination_data['pages']:
            # we need to query for next page
            has_next_page = True

        # get the relevant data from the response and populate it into data_dict
        data: list[dict] = response_data[1]
        print(f'Received {len(data)} entries in response')
        for entry in data:
            year = int(entry['date'])
            value = entry['value']
            indicator_data.append({
                'country': country_code,
                'year': year,
                'value': value
            })
    else:
        print(f'Could not get data for {country_code}, received status {response.status_code}')

    return has_next_page


def load_athletes_data() -> pd.DataFrame:
    url = 'https://storage.googleapis.com/edulabs-public-datasets/athlete_events.zip'

    converters = {
        "Sex": lambda s: s == 'M',  # return True if Male, false if Female
        "Season": lambda s: s == 'Summer'  # return True if Summer, false if Winter
    }
    dtypes = {
        "ID": "int32",
        "Age": "Int8",
        "Height": "float32",
        "Weight": "float32",
        "Year": "Int16",
        "Medal": "category"
    }
    usecols = [
        'ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC',
        'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'
    ]  # all the columns except for "Games" which is redundant

    df = pd.read_csv(url, usecols=usecols, converters=converters, dtype=dtypes)

    df.rename(columns={"Sex": "male", "Season": "summer"}, inplace=True)
    df.rename(columns={col: col.lower() for col in df.columns}, inplace=True)

    return df


if __name__ == '__main__':
    df = run(GDP_INDICATOR)
    df.to_csv("gdp_data.csv")
    print("done")