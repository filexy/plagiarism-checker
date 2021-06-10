# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Uploads(models.Model):
    title = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='documents/')
    authors = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploads'
class Checker(models.Model):
    file = models.FileField(upload_to='checker/')

    class Meta:
        managed = False
        db_table = 'checker'
