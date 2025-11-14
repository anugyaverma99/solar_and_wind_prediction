from django import forms

class EnergyPredictionForm(forms.Form):
    # Wind inputs
    air_density = forms.FloatField(label="Air Density (kg/m³)")
    wind_speed = forms.FloatField(label="Wind Speed (m/s)")
    
    # Solar inputs
    temperature = forms.FloatField(label="Temperature (°C)")
    humidity = forms.FloatField(label="Humidity (%)")
    ground_radiation_intensity = forms.FloatField(label="Ground Radiation Intensity (W/m²)")
    upper_atmospheric_radiation_intensity = forms.FloatField(label="Upper Atmospheric Radiation Intensity (W/m²)")

    # Date inputs
    year = forms.IntegerField(label="Year")
    month = forms.IntegerField(label="Month", min_value=1, max_value=12)
    day = forms.IntegerField(label="Day", min_value=1, max_value=31)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
