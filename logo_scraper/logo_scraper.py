# scrape url for logo images from a website according to the given list of company names
# make a list of company names from a csv file

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

df = pd.read_csv("top_holdings.csv", encoding="utf-8")
print(df.columns)  # Add this line to check column names
companies = df["0"].tolist()

print(companies)
