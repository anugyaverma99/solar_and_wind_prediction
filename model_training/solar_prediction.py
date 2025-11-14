import pandas as pd
import joblib

# Load the trained solar power model
model = joblib.load('C:/Users/DELL/Documents/django_project/energy_project/models/solar_power_model.pkl')

# Sample input data (make sure humidity is fraction, not percentage)
input_data = {
    'temperature': [25.0],                    # degrees Celsius
    'humidity': [0.01],                       # 1% humidity as fraction
    'ground radiation intensity': [500.0],   # W/m²
    'Upper atmospheric radiation intensity': [120.0],  # W/m²
    'Year': [2024],
    'Month': [10],
    'Day': [15]
}

input_df = pd.DataFrame(input_data)

# Predict solar power generation
predicted_power = model.predict(input_df)[0]

print(f"Predicted Photovoltaic Power Generation: {predicted_power:.2f} kW")
