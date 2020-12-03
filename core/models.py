from django.db import models

# Create your models here.
class Trip(models.Model):
    trip_from = models.CharField(max_length=200)
    to = models.CharField(max_length=200)
    at = models.DateTimeField()

    def __str__(self):
        return f'{self.trip_from} to {self.to} at {self.at}'
