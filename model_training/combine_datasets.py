import pandas as pd
from glob import glob

# Dataset folder path (use absolute path)
dataset_folder = 'C:/Users/DELL/Documents/django_project/datasets/'

def load_and_combine_excel_sheets(file_pattern):
    all_files = glob(dataset_folder + file_pattern)
    print(f"Files found for pattern {file_pattern}: {all_files}")
    if not all_files:
        raise FileNotFoundError(f"No files found matching pattern {file_pattern}")
    
    df_list = []
    for file in all_files:
        df = pd.read_excel(file)
        df_list.append(df)
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

# Load wind data (files starting with 'Wind')
wind_df = load_and_combine_excel_sheets('Wind*.xlsx')

# Load solar data (files starting with 'Photovoltaic')
solar_df = load_and_combine_excel_sheets('Photovoltaic*.xlsx')

# Parse 'years' column to datetime and drop 'time' and 'years' columns
wind_df['Datetime'] = pd.to_datetime(wind_df['years'])
wind_df = wind_df.drop(columns=['time', 'years'])

solar_df['Datetime'] = pd.to_datetime(solar_df['years'])
solar_df = solar_df.drop(columns=['time', 'years'])

# Save combined cleaned datasets as CSV files
wind_df.to_csv(dataset_folder + 'wind_combined.csv', index=False)
solar_df.to_csv(dataset_folder + 'solar_combined.csv', index=False)

print("✅ Combined wind and solar datasets saved in:", dataset_folder)
