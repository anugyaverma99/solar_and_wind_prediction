
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('predict/', views.predict_energy, name='predict_energy'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
     path('predict/result/<int:prediction_id>/', views.prediction_result, name='prediction_result'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('past_predictions/', views.past_predictions_view, name='past_predictions'),


]
