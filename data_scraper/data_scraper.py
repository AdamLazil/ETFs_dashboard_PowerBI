# data scraper in python
# this script scrapes data from a website and saves it to a CSV file
# I want to for each symbol in a list, scrape the tables which is available on the website

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
