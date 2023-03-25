from django.db import models

class Group(models.Model):
    category = models.CharField(max_length=6, blank=False)
    name_group = models.CharField(max_length=12, blank=False)
    url = models.CharField(max_length=60, blank=False)

