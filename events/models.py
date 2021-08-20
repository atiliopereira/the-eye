from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    session_id = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    data = models.JSONField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'{self.category} - {self.name} by {self.session_id} at {self.timestamp}'
