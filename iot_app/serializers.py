from rest_framework import serializers
from .models import DistanceData

class DistanceMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistanceData#DistanceMeasurement
        fields = ['distance', 'timestamp']