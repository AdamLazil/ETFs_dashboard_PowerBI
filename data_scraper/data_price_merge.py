# function for merging data from several ISINs into a single CSV file

import pandas as pd
import os
import glob

folder_path = "E:/UCENI/Engeto/datovaAkademie/data_isin"
output_path = "E:/UCENI/Engeto/datovaAkademie/ETFs_dashboard/ETFs_dashboard_PowerBI/data_files/csv_files/price_merged_data.csv"
isin_list = [
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


def merge_etfprice_data(folder_path, output_path, isin_list):
    """
    Merges ETF price data from multiple CSV files into a single CSV file.

    Parameters:
        folder_path (str): Path to the folder containing the CSV files.
        output_path (str): Path where the merged CSV file will be saved.
        isin_list (list of str): List of ISIN codes to filter the CSV files.

    Returns:
        None. The merged data is saved to the specified output_path.
    """
    all_data = []

    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    for file in csv_files:
        filename = os.path.basename(file)
        isin = filename.split("_")[0]
        if isin in isin_list:
            df = pd.read_csv(file)
            df["ISIN"] = isin
            all_data.append(df)
        else:
            continue

    if all_data:
        merged_df = pd.concat(all_data, ignore_index=True)
        merged_df.to_csv(output_path, index=False)
        print(f"Data merged and saved to {output_path}")
    else:
        print("No data to merge.")


def main():
    merge_etfprice_data(folder_path, output_path, isin_list)


if __name__ == "__main__":
    main()
