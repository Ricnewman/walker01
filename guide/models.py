"""
Django settings for TravelAid project.

# Author: Richard Newman,
# Student ID: D12124811,
# Undergraduate Course: DT249/4.
# Module: Final Year Project.
# Supervisor: Mark Foley.
# College: Dublin Institute of Technology, Kevin Street.
# Year: 2016.

"""

from django.db import models

class Journey(models.Model):
    source_add = models.CharField(max_length=500)
    destination_add = models.CharField(max_length=500)

    def __str__(self):
        return self.source_add + ' - ' + self.destination_add

class Route(models.Model):
    street_name = models.CharField(max_length=1000)
    intersection = models.CharField(max_length=1000)

    def __str__(self):
        return self.street_name + ' - ' + self.intersection

class Waypoint(models.Model):
    street_name = models.ForeignKey(Route, on_delete=models.CASCADE)
    poi_name = models.CharField(max_length=500)
    lat = models.DecimalField(max_digits=20, decimal_places=10, default=0.00)
    lon = models.DecimalField(max_digits=20, decimal_places=10,default=0.00)

    def __str__(self):
        return self.poi_name





