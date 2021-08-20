from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from events.models import Event
from events.serializers import EventSerializer


class EventsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Create Event object from JSON data
    """

    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        create_event_task.apply_async(args=(request.data,))

        return Response(None, status=status.HTTP_200_OK)
