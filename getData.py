import urllib.request
import gzip
import shutil
import pandas as pd
import numpy as np
import os

def get_data():
    # Define the URL prefix and file extension
    url_prefix = 'https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.'
    file_extension = '.csv.gz'
    data_dir = 'data'

    # Define an empty list to hold the monthly DataFrames
    monthly_dfs = []

    # Create the data directory if it does not exist
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    # Loop through each month from January 1996 to December 2022
    for year in range(1996, 2023):
        for month in range(1, 13):
            # Create the URL for the current month's data file
            url = url_prefix + f"{year:04d}{month:02d}" + file_extension
            # Define the file name for the current month's data file
            file_name = f"{data_dir}/synop.{year:04d}{month:02d}.csv"
            print(f"Downloading {file_name}")
            # Download the file
            with urllib.request.urlopen(url) as response, open(file_name + '.gz', 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            # Unzip the file
            with gzip.open(file_name + '.gz', 'rb') as f_in, open(file_name, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            # Load the data file into a Pandas DataFrame
            df = pd.read_csv(file_name, sep=';')
            # Convert the temperature from Kelvin to Celsius, skipping over any invalid values
            df['t'] = pd.to_numeric(df['t'], errors='coerce')
            df['t'] = np.where(df['t'].isna(), np.nan, df['t'] - 273.15)
            # Convert the date column to a datetime object
            df['date'] = pd.to_datetime(df['date'], format='%Y%m%d%H%M%S')
            # Add the DataFrame to the list of monthly DataFrames
            monthly_dfs.append(df)

    # Merge all the monthly DataFrames into one DataFrame
    merged_df = pd.concat(monthly_dfs)

    # Save the merged DataFrame to a CSV file
    merged_df.to_csv(f"{data_dir}/merged_data.csv", index=False)
