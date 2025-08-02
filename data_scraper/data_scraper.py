# data scraper in python
# this script scrapes data from a website and saves it to a CSV file
# I want to for each symbol in a list, scrape the tables which is available on the website

# table class for data is 'table etf-data-table'
# table class for Top 10 Holdings is 'table mb-0' and <h3> is 'Top 10 Holdings'
# table class for countries is 'table mb-0 ' and <h3> is 'Countries'
# table for sectors is 'table mb-0 ' and <h3> is 'Sectors'

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# list of isin codes
isin_codes = [
    "IE00BKWQ0L68",
    "DE000A0F5UK5",
    "LU0292100806",
    "IE00BKWQ0F09",
    "DE000A0H08M3",
    "LU1834988278",
    "DE000A0F5UJ7",
    "LU1829219390",
    "IE00BKWQ0G16",
    "DE000A0Q4R36",
    "IE00BKWQ0H23",
    "DE000A0H08F7",
    "IE00B5MJYX09",
    "DE000A0H08Q4",
    "IE00BKWQ0K51",
    "IE00BKWQ0N82",
    "LU1834988609",
]


# help function for saving data to CSV
def save_to_csv(df, isin, filename):
    filename = f"{isin}_{filename}.csv"
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


# function to scrape data for a given ISIN code
def scrape_data(isin):
    url = f"https://www.justetf.com/en/etf-profile.html?isin={isin}#overview"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {isin}: {e}")
        return None

    soup = BeautifulSoup(response.content, "lxml")

    tables_to_find = {
        "data_table": "table.etf-data-table",
        "top_holdings": {"class": "table mb-0", "header": "Top 10 Holdings"},
        "countries": {"class": "table mb-0", "header": "Countries"},
        "sectors": {"class": "table mb-0", "header": "Sectors"},
    }
    # Data table has unique class
    try:
        data_table = soup.select_one(tables_to_find["data_table"])
        if data_table:
            df_data = pd.read_html(str(data_table))[0]
            save_to_csv(df_data, isin, "data_table")
    except Exception as e:
        print(f"Error processing data table for {isin}: {e}")

    # rest of tables are identified by class and header
    for key in ["top_holdings", "countries", "sectors"]:
        try:
            table = soup.find("h3", text=tables_to_find[key]["header"])
            if table:
                table_data = table.find_next(
                    "table", class_=tables_to_find[key]["class"]
                )
                if table_data:
                    df_table = pd.read_html(str(table_data))[0]
                    save_to_csv(df_table, isin, key)
            else:
                print(f"No {tables_to_find[key]['header']} table found for {isin}")
        except Exception as e:
            print(f"Error processing {key} for {isin}: {e}")

    time.sleep(1)  # Sleep to avoid overwhelming the server


# main function to iterate over ISIN codes
def main():
    for isin in isin_codes:
        print(f"Scraping data for ISIN: {isin}")
        scrape_data(isin)
        time.sleep(2)  # Sleep between requests to avoid rate limiting


if __name__ == "__main__":
    main()
# This script will scrape data for each ISIN code in the list and save the results to CSV files.
