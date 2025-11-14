from django.db import models
from django.contrib.auth.models import User

class EnergyPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wind_power = models.FloatField()
    solar_power = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # Optional: save input values too if you want
    temperature = models.FloatField()
    humidity = models.FloatField()
    ground_radiation_intensity = models.FloatField()
    upper_atmospheric_radiation_intensity = models.FloatField()
    air_density = models.FloatField()
    wind_speed = models.FloatField()
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    def __str__(self):
        return f"Prediction by {self.user.username} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
