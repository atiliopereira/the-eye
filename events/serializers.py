from rest_framework import serializers

from events.models import Event, Category
from the_eye.globals import DATETIME_FORMAT


class EventSerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    session_id = serializers.CharField()
    name = serializers.CharField()
    data = serializers.JSONField()
    timestamp = serializers.DateTimeField(format=DATETIME_FORMAT)

    class Meta:
        model = Event
        fields = ('session_id', 'category', 'name', 'data', 'timestamp')

    def create(self, validated_data):
        category = Category.objects.get(name=validated_data.get('category'))

        return Event(session_id=validated_data.get('session_id'), category=category, name=validated_data.get('name'),
                     data=validated_data.get('data'), timestamp=validated_data.get('timestamp'))
