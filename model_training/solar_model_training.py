import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

# Load data
solar_df = pd.read_csv('datasets/solar_combined.csv')
solar_df['Datetime'] = pd.to_datetime(solar_df['Datetime'])
solar_df['Year'] = solar_df['Datetime'].dt.year
solar_df['Month'] = solar_df['Datetime'].dt.month
solar_df['Day'] = solar_df['Datetime'].dt.day

features = ['temperature', 'humidity', 'ground radiation intensity',
            'Upper atmospheric radiation intensity', 'Year', 'Month', 'Day']
target = 'Photovoltaic power generation'

X = solar_df[features]
y = solar_df[target]

# Split into train/test (to simulate real eval)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load your trained model
model = joblib.load('energy_project/models/solar_power_model.pkl')

# Predict on test set
y_pred = model.predict(X_test)

# Plot scatter
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel('Actual Solar Power Generation')
plt.ylabel('Predicted Solar Power Generation')
plt.title('Actual vs Predicted Solar Power')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Diagonal line
plt.show()

# Print mean absolute error
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error on Test Set: {mae:.2f}")
