from django.contrib import admin
from .models import Workout, Schedule, Activity, Friend, Photo
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Workout)
admin.site.register(Schedule)
admin.site.register(Activity)
admin.site.register(Friend)
admin.site.register(Photo)