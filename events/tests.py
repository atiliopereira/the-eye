from datetime import datetime

from django.test import TestCase

from events.models import Category, Event
from the_eye.globals import DATETIME_FORMAT


class CategoryTest(TestCase):

    def create_category(self, name="Test name"):
        return Category(name=name)

    def test_category_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertTrue((c.__str__(), f'{c.name}'))


class EventTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.category = Category.objects.create(name="page interaction")
        self.session_id = "e2085be5-9137-4e4e-80b5-f1ffddc25423"
        self.name = "pageview"
        self.data = {
            "host": "www.consumeraffairs.com",
            "path": "/",
        }
        self.timestamp = datetime.strptime("2021-01-01 09:15:27.243860", DATETIME_FORMAT)

    def create_event(self):
        return Event(session_id=self.session_id, category=self.category, name=self.name, data=self.data,
                     timestamp=self.timestamp)

    def test_event_creation(self):
        e = self.create_event()
        self.assertTrue(isinstance(e, Event))
        self.assertTrue((e.__str__(), f'{e.category} - {e.name} by {e.session_id} at {e.timestamp}'))

    def get_json_sample(self):
        json_string = """ 
{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "pageview",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/"
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}
"""
        return json.loads(json_string)

    def test_event_multiple_creation(self):
        """
        Test 1000 Event insertions
        """
        processes = []
        for i in range(1000):
            p = Process(target=self.client.post, args=('/events/', self.get_json_sample()))
            p.start()
            processes.append(p)

        for i, p in enumerate(processes):
            p.join()
