import pandas as pd
import joblib

# Load trained model
model = joblib.load('energy_project/models/solar_power_model.pkl')

# Load dataset
data = pd.read_csv('datasets/solar_combined.csv')

# If dataset has a datetime column, extract Year, Month, Day
if 'Datetime' in data.columns:
    data['Datetime'] = pd.to_datetime(data['Datetime'], errors='coerce')
    data['Year'] = data['Datetime'].dt.year
    data['Month'] = data['Datetime'].dt.month
    data['Day'] = data['Datetime'].dt.day

# Select 10 random rows for comparison
sample = data.sample(10, random_state=42)

# Define feature columns safely (ignore if any missing)
features = ['temperature', 'humidity', 'ground radiation intensity',
            'Upper atmospheric radiation intensity', 'Year', 'Month', 'Day']
features = [f for f in features if f in sample.columns]

# Split X and y
X = sample[features]
y_true = sample['Photovoltaic power generation']

# Make predictions
y_pred = model.predict(X)

# Display comparison
results = pd.DataFrame({
    'Actual': y_true.round(2),
    'Predicted': y_pred.round(2)
})

print("\n--- Solar Model Validation ---")
print(results)
print("\nMean Absolute Error:", (abs(results['Actual'] - results['Predicted'])).mean().round(2))
