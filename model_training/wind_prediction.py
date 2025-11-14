import joblib
import pandas as pd

# Load the trained model
model_path = 'C:/Users/DELL/Documents/django_project/models/wind_power_model.pkl'
model = joblib.load(model_path)

# Prepare new input data (replace with real or user-input values)
new_data = {
    'air density': [1.18],   # example value (kg/m³)
    'wind speed': [7.5]      # example value (m/s)
}

# Convert to DataFrame (ensure column names match training data exactly)
input_df = pd.DataFrame(new_data)

# Predict power generation
predicted_power = model.predict(input_df)

print("Predicted Wind Power Generation:", predicted_power[0])
