from django.db import models
from django.contrib.auth import get_user_model


class Location(models.Model):
    Latitude = models.FloatField()
    Altitude = models.FloatField()


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Event_member(models.Model):
    user = models.ManyToManyField(get_user_model())
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
