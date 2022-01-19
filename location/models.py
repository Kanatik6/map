from django.db import models
from django.contrib.gis.db.models import PointField


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = PointField(null=True) 

    def __str__(self):
        return self.name
