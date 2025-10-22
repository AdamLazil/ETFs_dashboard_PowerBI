![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/Library-BeautifulSoup4-green.svg)
![Pandas](https://img.shields.io/badge/Library-pandas-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

# 🧠 ETF Data Scraper

## Description

This project contains a Python script that automatically scrapes, cleans, and saves ETF data from justETF.com.
It loops through a list of ISIN codes, extracts the available data tables (general info, top holdings, countries, sectors), and saves them into clean CSV files for further analysis (e.g., in Power BI).

## 🚀 Key Features

- Automated ETF data scraping from justETF.com

- Support for multiple ISIN codes (batch processing)

- Extracts and stores:

  - 📊 **Main ETF data table** (table.etf-data-table)

  - 🏢 **Top 10 Holdings**

  - 🌍 **Countries**

  - 🧩 **Sectors**

- **Data cleaning and normalization** — adds ISIN to each table

- **Exports to CSV files** ready for analytics and visualization

- **Optional transformation** of the main table from row to column format

## ⚙️ Requirements

- Python 3.8+

- Libraries:

```bash
pip install requests beautifulsoup4 pandas lxml
```

## 🧩 Usage

1. Edit the list of ISIN codes in isin_codes:

```python
isin_codes = [
    "IE00BKWQ0L68",
    "DE000A0F5UK5",
    ...
]
```

2. Set the output directory for CSV files:

```python
output_dir = "E:/UCENI/Engeto/datovaAkademie/ETFs_dashboard/ETFs_dashboard_PowerBI/data_files/csv_files"
```

3. Run the script:

```bash
python etf_scraper.py
```

4. After execution, four CSV files will be created:

- data_table.csv

- top_holdings.csv

- countries.csv

- sectors.csv

5. The script will then automatically transform data_table.csv into:

```
transformed_data_table.csv
```

## 🔄 Data Transformation

The transform_csv() function reshapes the main ETF data (data_table.csv) from a row-based format into columns using pivot().
The result is a cleaner, more structured dataset suitable for Power BI or Excel dashboards.

## 📈 Example Use in Power BI

This project serves as a data source for an ETF Dashboard in Power BI, enabling:

- portfolio composition visualization,

- sector and country distribution analysis,

- trend tracking over time.

## 🧑‍💻 Author

Adam Lízal
Created as part of a personal data portfolio project — focused on web scraping, data cleaning, and analytics.

## 🏷️ GitHub Topics (tags)

```kotlin
python
web-scraping
data-analysis
data-cleaning
etf
finance
beautifulsoup
pandas
powerbi
automation
csv
```
