from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    # user = models.ForeignKey(User, related_name="activities", on_delete=models.CASCADE, null=True, blank=True)
    race = models.CharField(max_length=200, null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    workout_type = models.CharField(max_length=200, null=True, blank=True)
    distance = models.CharField(max_length=200, null=True, blank=True)
    # pace = models.CharField(max_length=200, null=True, blank=True)
    # duration = models.CharField(max_length=200, null=True, blank=True)
    # location = models.CharField(max_length=200, null=True, blank=True)

class Schedule(models.Model):
    user = models.ForeignKey(User, related_name="schedules", on_delete=models.CASCADE)
    distance = models.CharField(max_length=200)

class Workout(models.Model):
    user = models.ForeignKey(User, related_name="workouts", on_delete=models.CASCADE, null=True, blank=True)
    race = models.CharField(max_length=200, null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    workout_type = models.CharField(max_length=200, null=True, blank=True)
    distance = models.CharField(max_length=200, null=True, blank=True)
    pace = models.CharField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)