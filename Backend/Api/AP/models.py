from django.db import models
from unittest.util import _MAX_LENGTH


# Create your models here.
class Me(models.Model):
    SlackUsername = models.CharField(max_length=200)
    Backend = models.BooleanField()
    age = models.IntegerField()
    Bio = models.CharField(max_length= 200)