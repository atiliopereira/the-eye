from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from events.serializers import EventSerializer


class EventsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Create Event object from JSON data
    """

    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save().save()

        return Response(serializer.data, status=status.HTTP_200_OK)
