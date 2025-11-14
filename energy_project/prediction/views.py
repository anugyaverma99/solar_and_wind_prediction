from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EnergyPrediction

from django.utils import timezone
from .forms import RegisterForm, EnergyPredictionForm
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
wind_model_path = os.path.join(BASE_DIR, 'models', 'wind_power_model.pkl')
solar_model_path = os.path.join(BASE_DIR, 'models', 'solar_power_model.pkl')

wind_model = joblib.load(wind_model_path)
solar_model = joblib.load(solar_model_path)

@login_required(login_url='login')
def dashboard(request):
    prediction = None
    if request.method == 'POST':
        form = EnergyPredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            wind_input = pd.DataFrame({
                'air density': [data['air_density']],
                'wind speed': [data['wind_speed']],
            })

            solar_input = pd.DataFrame({
                'temperature': [data['temperature']],
                'humidity': [data['humidity']],
                'ground radiation intensity': [data['ground_radiation_intensity']],
                'Upper atmospheric radiation intensity': [data['upper_atmospheric_radiation_intensity']],
                'Year': [data['year']],
                'Month': [data['month']],
                'Day': [data['day']],
            })

            wind_pred = wind_model.predict(wind_input)[0]
            solar_pred = solar_model.predict(solar_input)[0]

            prediction = {
                'wind_power': round(wind_pred, 2),
                'solar_power': round(solar_pred, 2),
            }

            # Save prediction to DB
            EnergyPrediction.objects.create(
                user=request.user,
                wind_power=wind_pred,
                solar_power=solar_pred,
                temperature=data['temperature'],
                humidity=data['humidity'],
                ground_radiation_intensity=data['ground_radiation_intensity'],
                upper_atmospheric_radiation_intensity=data['upper_atmospheric_radiation_intensity'],
                air_density=data['air_density'],
                wind_speed=data['wind_speed'],
                year=data['year'],
                month=data['month'],
                day=data['day'],
                timestamp=timezone.now()
            )
    else:
        form = EnergyPredictionForm()

    past_predictions = EnergyPrediction.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'prediction/dashboard.html', {
        'form': form,
        'prediction': prediction,
        'past_predictions': past_predictions,
    })


@login_required
def predict_energy(request):
    if request.method == 'POST':
        form = EnergyPredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            wind_input = pd.DataFrame({
                'air density': [data['air_density']],
                'wind speed': [data['wind_speed']],
            })

            solar_input = pd.DataFrame({
                'temperature': [data['temperature']],
                'humidity': [data['humidity']],
                'ground radiation intensity': [data['ground_radiation_intensity']],
                'Upper atmospheric radiation intensity': [data['upper_atmospheric_radiation_intensity']],
                'Year': [data['year']],
                'Month': [data['month']],
                'Day': [data['day']],
            })

            wind_pred = wind_model.predict(wind_input)[0]
            solar_pred = solar_model.predict(solar_input)[0]

            # Save prediction to DB
            prediction = EnergyPrediction.objects.create(
                user=request.user,
                wind_power=wind_pred,
                solar_power=solar_pred,
                temperature=data['temperature'],
                humidity=data['humidity'],
                ground_radiation_intensity=data['ground_radiation_intensity'],
                upper_atmospheric_radiation_intensity=data['upper_atmospheric_radiation_intensity'],
                air_density=data['air_density'],
                wind_speed=data['wind_speed'],
                year=data['year'],
                month=data['month'],
                day=data['day'],
                timestamp=timezone.now()
            )

            # Redirect to the results page
            return redirect('prediction_result', prediction_id=prediction.id)
    else:
        form = EnergyPredictionForm()

    return render(request, 'prediction/predict.html', {'form': form})


import json

def prediction_result(request, prediction_id):
    prediction = get_object_or_404(EnergyPrediction, pk=prediction_id)

    # Prepare JSON string safely
    prediction_json = json.dumps({
        'wind_power': prediction.wind_power or 0,
        'solar_power': prediction.solar_power or 0
    })

    context = {
        'prediction': prediction,
        'prediction_json': prediction_json,  # pass JSON string here
    }
    return render(request, 'prediction/prediction_result.html', context)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'prediction/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'prediction/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def landing_page(request):
    return render(request, 'prediction/landing.html')


@login_required
def past_predictions_view(request):
    past_predictions = EnergyPrediction.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'prediction/past_predictions.html', {'past_predictions': past_predictions})
