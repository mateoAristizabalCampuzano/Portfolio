from django.db import models


# Create your models here.
from django.db.models import  CharField, URLField


class Project (models.Model):
    objects = None
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    url = URLField(blank=True)