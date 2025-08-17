# scrape url for logo images from a website according to the given list of company names
# make a list of company names from a csv file

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from tqdm import tqdm

file_path = "E:/UCENI/Engeto/datovaAkademie/ETFs_dashboard/ETFs_dashboard_PowerBI/data_files/csv_files/top_holdings.csv"


def get_logo_url(company_name):
    """Fetch the logo URL for a given company name from Wikimedia Commons."""
    try:
        search_url = f"https://commons.wikimedia.org/wiki/Special:Search?search={company_name}+logo&go=Go"
        response = requests.get(search_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        img_tag = soup.find("img", class_="mw-file-description")
        if img_tag and "src" in img_tag.attrs:
            img_url = img_tag["src"]
            return img_url
    except Exception as e:
        print(f"Error fetching logo for {company_name}: {e}")
    return None


def scrape_logos():
    """Scrape logos for companies listed in a CSV file."""
    df = pd.read_csv(file_path, encoding="utf-8")

    if "logo_url" in df.columns:
        df["logo_url"] = ""

    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Scraping logos"):
        company_name = row["0"]
        url = get_logo_url(company_name)
        if url:
            df.at[idx, "logo_url"] = url
        else:
            df.at[idx, "logo_url"] = "Logo not found"
        time.sleep(1)  # To avoid overwhelming the server with requests

    # Save the updated DataFrame to a new CSV file
    output_file_path = "E:/UCENI/Engeto/datovaAkademie/ETFs_dashboard/ETFs_dashboard_PowerBI/data_files/csv_files/top_holdings_with_logos.csv"
    df.to_csv(output_file_path, index=False, encoding="utf-8")
    print(f"Logo URLs saved to {output_file_path}")


# Note: Ensure that the output directory exists before running the script.

if __name__ == "__main__":
    scrape_logos()
# This script is designed to scrape logo images from Wikimedia Commons based on company names
# listed in a CSV file. It fetches the logo URLs and saves them back to a new CSV file.
# Make sure to have the required libraries installed: requests, beautifulsoup4, pandas, tqdm.
