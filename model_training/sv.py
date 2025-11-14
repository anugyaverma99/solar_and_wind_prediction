import pandas as pd

solar_df = pd.read_csv('C:/Users/DELL/Documents/django_project/datasets/solar_combined.csv')

print(solar_df['Photovoltaic power generation'].describe())
