from django.urls import path
from .views import index_view, meter_view, receive_sensor_data, latest_distance_view

urlpatterns = [
    path('', index_view, name='index'),  # Home page
    path('meter/', meter_view, name='meter'),  # Meter page
    path('api/sensor/', receive_sensor_data, name='receive_sensor_data'),  # Endpoint to receive sensor data
    path('api/latest-distance/', latest_distance_view, name='latest_distance'),  # Endpoint to get latest distance
]