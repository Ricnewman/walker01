from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Journey,Route,Waypoint
from .serializers import JourneySerializer,RouteSerializer,WaypointSerializer


# List objects or create a new one.
class JourneyList(APIView):

    def get(self, request):
        journeys = Journey.objects.all()
        serializer = JourneySerializer(journeys, many=True)
        return Response(serializer.data)


    def post(self):
        pass


class RouteList(APIView):

    def get(self, request):
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)


    def post(self):
        pass


class WaypointList(APIView):

    def get(self, request):
        waypoints = Waypoint.objects.all()
        serializer = WaypointSerializer(waypoints, many=True)
        return Response(serializer.data)


    def post(self, request):
        pass



