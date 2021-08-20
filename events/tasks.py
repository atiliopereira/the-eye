from events.serializers import EventSerializer
from the_eye.celery import app


@app.task(name="create_event_task", bind=True, default_retry_delay=1, max_retries=5)
def create_event_task(self, data):
    serializer = EventSerializer(data=data)

    if serializer.is_valid():
        serializer.save().save()
