from .models import Activity, Schedule, Workout, Friend, Photo
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins
from .serializers import ActivitySerializer, ScheduleSerializer, WorkoutSerializer, UserSerializer, FriendSerializer, PhotoSerializer

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

class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UserSerializer

class FriendCreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FriendSerializer

    def perform_destroy(self, serializer):
        serializer.delete(follower=self.request.user)

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class FriendViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Friend.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = FriendSerializer

class PhotoCreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PhotoSerializer

    def perform_destroy(self, serializer):
        serializer.delete(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PhotoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Photo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = PhotoSerializer
