from rest_framework import serializers
from .models import Journey,Route,Waypoint

class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ('source_add','destination_add')

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('street_name','intersection')

class WaypointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waypoint
        fields = ('poi_name','lat','lon')



