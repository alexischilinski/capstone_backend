from rest_framework import routers
from .api import (ActivityViewSet, ActivityCreateDestroyViewSet, 
                ScheduleViewSet, WorkoutViewSet, WorkoutCreateDestroyViewSet, 
                WorkoutCRUDViewSet, UserViewSet, FriendViewSet, PhotoCRUDViewSet, 
                PhotoViewSet, FollowerViewSet, ScheduleCRUDViewSet,
                IncomingMessageCRUDViewSet, OutoingMessageCRUDViewSet)

router = routers.DefaultRouter()
router.register('api/activities', ActivityViewSet, 'activities')
router.register('api/cdactivities', ActivityCreateDestroyViewSet, 'createdestroyactivities')
router.register('api/schedules', ScheduleViewSet, 'schedules')
router.register('api/crudschedules', ScheduleCRUDViewSet, 'crudschedules')
router.register('api/workouts', WorkoutViewSet, 'workouts')
router.register('api/crudworkouts', WorkoutCRUDViewSet, 'crudworkouts')
router.register('api/users', UserViewSet, 'users')
router.register('api/friends', FriendViewSet, 'friends')
router.register('api/following', FollowerViewSet, 'following')
router.register('api/crudphotos', PhotoCRUDViewSet, 'crudphoto')
router.register('api/photos', PhotoViewSet, 'photos')
router.register('api/incoming', IncomingMessageCRUDViewSet, 'incoming')
router.register('api/outgoing', OutoingMessageCRUDViewSet, 'outgoing')

urlpatterns = router.urls