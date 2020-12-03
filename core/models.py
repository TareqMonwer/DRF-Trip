from datetime import datetime, date
from django.db import models


class Trip(models.Model):
    trip_from = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def duration(self):
        d = datetime.combine(date.min, self.end_time) - \
            datetime.combine(date.min, self.start_time)
        return f'{d}'
    
    def __str__(self):
        return f'{self.trip_from} tour for {self.duration()}'
