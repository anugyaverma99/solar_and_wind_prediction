import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Step 1: Load cleaned dataset
wind_df = pd.read_csv('C:/Users/DELL/Documents/django_project/datasets/wind_combined.csv')

# Step 2: Define input and output columns
X = wind_df[['air density', 'wind speed']]   # features
y = wind_df['Power generation']              # target

# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Predict on test set
y_pred = model.predict(X_test)

# Step 6: Evaluate performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation Results:")
print(f"MAE: {mae:.3f}")
print(f"MSE: {mse:.3f}")
print(f"R² Score: {r2:.3f}")

# Step 7: Save trained model for Django use later
joblib.dump(model, 'C:/Users/DELL/Documents/django_project/models/wind_power_model.pkl')

print("\nModel training completed and saved successfully!")
