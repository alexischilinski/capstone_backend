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
    user = models.ForeignKey(User, related_name="schedules", on_delete=models.CASCADE, null=True, blank=True)
    distance = models.CharField(max_length=200, null=True, blank=True)
    race_name = models.CharField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(null=True, blank=True)

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

class Friend(models.Model):
    follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

class Photo(models.Model):
    user = models.ForeignKey(User, related_name="photo", on_delete=models.CASCADE, null=True, blank=True)
    photo = models.TextField(null=True, blank=True)

class Message(models.Model):
    receiver = models.ForeignKey(User, related_name="incoming", on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(User, related_name="outgoing", on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(blank=True, null=True)
    read = models.BooleanField(blank=True, null=True)
    subject = models.CharField(max_length=200, null=True, blank=True)