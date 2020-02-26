from rest_framework import routers
from .api import ActivityViewSet, ActivityCreateDestroyViewSet, ScheduleViewSet, ScheduleCreateDestroyViewSet, WorkoutViewSet, WorkoutCreateDestroyViewSet, UserViewSet, FriendCreateDestroyViewSet, FriendViewSet, PhotoCreateDestroyViewSet, PhotoViewSet

router = routers.DefaultRouter()
router.register('api/activities', ActivityViewSet, 'activities')
router.register('api/cdactivities', ActivityCreateDestroyViewSet, 'createdestroyactivities')
router.register('api/schedules', ScheduleViewSet, 'schedules')
router.register('api/cdschedules', ScheduleCreateDestroyViewSet, 'createdestroyschedules')
router.register('api/workouts', WorkoutViewSet, 'workouts')
router.register('api/cdworkouts', WorkoutCreateDestroyViewSet, 'createdestroyworkouts')
router.register('api/users', UserViewSet, 'users')
router.register('api/friends', FriendViewSet, 'friends')
router.register('api/cdfriends', FriendCreateDestroyViewSet, 'createdestroyfriends')
router.register('api/cudphotos', PhotoCreateDestroyViewSet, 'cudphoto')
router.register('api/photos', PhotoViewSet, 'photos')

urlpatterns = router.urls