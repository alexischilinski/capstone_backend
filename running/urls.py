from rest_framework import routers
from .api import ActivityViewSet, ActivityCreateDestroyViewSet, ScheduleViewSet, ScheduleCreateDestroyViewSet

router = routers.DefaultRouter()
router.register('api/activities', ActivityViewSet, 'activities')
router.register('api/cdactivities', ActivityCreateDestroyViewSet, 'createdestroyactivities')
router.register('api/schedules', ScheduleViewSet, 'schedules')
router.register('api/cdschedules', ScheduleCreateDestroyViewSet, 'createdestroyschedules')

urlpatterns = router.urls