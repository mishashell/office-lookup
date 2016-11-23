from django.db import models


class Office(models.Model):
    # Offices data from Setting and sharedesk
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    latitude = models.CharField(max_length=12)
    longtitude = models.CharField(max_length=12)
