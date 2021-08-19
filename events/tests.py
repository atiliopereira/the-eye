from datetime import datetime

from django.test import TestCase

from events.models import Category, Event


class CategoryTest(TestCase):

    def create_category(self, name="Test name"):
        return Category.objects.create(name=name)

    def test_category_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertTrue((c.__str__(), f'{c.name}'))


class EventTest(TestCase):

    def create_event(self):
        session_id = "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        name = "pageview",
        category_name = "page interaction"
        data = {
                   "host": "www.consumeraffairs.com",
                   "path": "/",
               }
        timestamp_str = "2021-01-01 09:15:27.243860"
        category = Category.objects.create(name=category_name)
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
        return Event.objects.create(session_id=session_id, category=category, name=name, data=data,
                                    timestamp=timestamp)

    def test_event_creation(self):
        e = self.create_event()
        self.assertTrue(isinstance(e, Event))
        self.assertTrue((e.__str__(), f'{e.category} - {e.name} by {e.session_id} at {e.timestamp}'))

