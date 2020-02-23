from .models import Activity, Schedule, Workout
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins
from .serializers import ActivitySerializer, ScheduleSerializer, WorkoutSerializer

class ActivityCreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ActivitySerializer

    def perform_destroy(self, serializer):
        serializer.delete(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ActivityViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Activity.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ActivitySerializer

class ScheduleCreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ScheduleSerializer

    def perform_destroy(self, serializer):
        serializer.delete(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ScheduleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Schedule.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScheduleSerializer

class WorkoutViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Workout.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = WorkoutSerializer

class WorkoutCreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = WorkoutSerializer

    def perform_destroy(self, serializer):
        serializer.delete(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
