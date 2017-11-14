from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Emailadress = models.CharField(max_length=255)
    Age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
