from django.db import models

class DistanceData(models.Model):
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Distance: {self.distance} cm"