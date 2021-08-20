from django.urls import path, include
from rest_framework import routers

from events.views import EventsViewSet

router = routers.SimpleRouter()
router.register(r'events', EventsViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
]
