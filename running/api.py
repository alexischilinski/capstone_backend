from .models import Activity, Schedule
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins
from .serializers import ActivitySerializer, ScheduleSerializer

class ActivityCreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Activity.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ActivitySerializer

    def perform_destroy(self, serializer):
        serializer.delete(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ActivityViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Activity.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ActivitySerializer

class ScheduleCreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Schedule.objects.all()
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