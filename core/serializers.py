from rest_framework import serializers

from .models import Trip


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('id', 'trip_from', 'start_time', 'end_time', 'duration')
