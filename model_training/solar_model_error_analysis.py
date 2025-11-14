import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split

# Load dataset
solar_df = pd.read_csv('datasets/solar_combined.csv')
solar_df['Datetime'] = pd.to_datetime(solar_df['Datetime'])
solar_df['Year'] = solar_df['Datetime'].dt.year
solar_df['Month'] = solar_df['Datetime'].dt.month
solar_df['Day'] = solar_df['Datetime'].dt.day

# Features and target
features = ['temperature', 'humidity', 'ground radiation intensity',
            'Upper atmospheric radiation intensity', 'Year', 'Month', 'Day']
target = 'Photovoltaic power generation'

X = solar_df[features]
y = solar_df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load your trained model
model = joblib.load('energy_project/models/solar_power_model.pkl')

# Predict on test set
y_pred = model.predict(X_test)

# Prepare results for error analysis
results_df = X_test.copy()
results_df['Actual'] = y_test.values
results_df['Predicted'] = y_pred
results_df['Residual'] = results_df['Actual'] - results_df['Predicted']

# Add Datetime for plotting
results_df['Datetime'] = solar_df.loc[results_df.index, 'Datetime']
results_df['Month'] = results_df['Datetime'].dt.month
results_df['Hour'] = results_df['Datetime'].dt.hour

# Plot residuals by month (seasonal pattern)
plt.figure(figsize=(10,6))
results_df.boxplot(column='Residual', by='Month')
plt.title('Residuals by Month (Seasonal Error Analysis)')
plt.suptitle('')
plt.xlabel('Month')
plt.ylabel('Prediction Error (Actual - Predicted)')
plt.show()

# Scatter residuals vs actual
plt.figure(figsize=(8,6))
plt.scatter(results_df['Actual'], results_df['Residual'], alpha=0.5)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Actual Solar Power Generation')
plt.ylabel('Residual (Error)')
plt.title('Residuals vs Actual Solar Power')
plt.show()

# Residuals by hour of day
plt.figure(figsize=(10,6))
results_df.boxplot(column='Residual', by='Hour')
plt.title('Residuals by Hour of Day')
plt.suptitle('')
plt.xlabel('Hour of Day')
plt.ylabel('Prediction Error (Actual - Predicted)')
plt.show()
