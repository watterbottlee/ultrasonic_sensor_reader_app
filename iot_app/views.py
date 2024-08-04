from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import DistanceData

def index_view(request):
    """Render the index page."""
    return render(request, 'iot_app/index.html')

def meter_view(request):
    """Render the meter page."""
    return render(request, 'iot_app/meter.html')

@csrf_exempt  # Disable CSRF protection for this view (not recommended for production)
def receive_sensor_data(request):
    """Receive sensor data via POST request and save it to the database."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            distance = data.get('distance')

            # Save the distance data to the database
            DistanceData.objects.create(distance=distance)

            print(f"Received Distance: {distance} cm")
            return JsonResponse({'status': 'success'})
        except Exception as e:
            print(f"Error processing data: {e}")
            return JsonResponse({'status': 'fail', 'error': str(e)}, status=500)

    return JsonResponse({'status': 'fail'}, status=400)

def latest_distance_view(request):
    """Retrieve the latest distance measurement."""
    try:
        latest_data = DistanceData.objects.latest('created_at')
        return JsonResponse({'distance': latest_data.distance})
    except DistanceData.DoesNotExist:
        return JsonResponse({'distance': 0})  # Return 0 if no data exists