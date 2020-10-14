import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=50)
    join_date = models.DateTimeField('Date account created')

    def __str__(self):
        return self.name + ' ' + self.id + ' ' + self.status
