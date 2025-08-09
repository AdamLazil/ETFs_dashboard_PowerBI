# Data scraper in python

## Description

This Python script scrapes ETF profile data from JustETF.com for a given list of ISIN codes and consolidates the results into CSV files.

It extracts four types of data for each ETF:

- _General ETF data table (fund details, key metrics)_

- _Top 10 holdings_

- _Countries allocation_

- _Sectors allocation_

**The script then:**

Merges the results of each category across all ISINs into a single CSV file.

Saves the output in a specified directory.

Transforms the general ETF data table into a pivoted format, where each ISIN becomes a single row and data keys are represented as columns.

## Purpose

The resulting CSV files are suitable for further analysis, reporting, or integration with visualization tools such as Power BI. This enables automated data collection and preparation for financial dashboards without manual downloading or copying from the website.

## Technologies and Libraries Used

requests – to retrieve HTML content from the target website

BeautifulSoup (bs4) – to parse and navigate the HTML structure

pandas – to extract, process, and merge table data

os & time – for file handling and request pacing
