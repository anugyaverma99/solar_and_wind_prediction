import pandas as pd

# Load combined data if not already in memory
wind_df = pd.read_csv('C:/Users/DELL/Documents/django_project/datasets/wind_combined.csv')
solar_df = pd.read_csv('C:/Users/DELL/Documents/django_project/datasets/solar_combined.csv')

# Convert Datetime to pandas datetime type
wind_df['Datetime'] = pd.to_datetime(wind_df['Datetime'])
solar_df['Datetime'] = pd.to_datetime(solar_df['Datetime'])

def extract_datetime_features(df):
    df['Year'] = df['Datetime'].dt.year
    df['Month'] = df['Datetime'].dt.month
    df['Day'] = df['Datetime'].dt.day
    # Uncomment if you have hour data and it is meaningful
    # df['Hour'] = df['Datetime'].dt.hour
    return df

wind_df = extract_datetime_features(wind_df)
solar_df = extract_datetime_features(solar_df)

print(wind_df.head())
print(solar_df.head())
