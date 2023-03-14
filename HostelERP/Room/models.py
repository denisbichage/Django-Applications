# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class room(models.Model):
    room_number = models.CharField(max_length=5, primary_key=True)
    capacity = models.CharField(max_length=5)
    vacancy = models.CharField(max_length=5)
    additional_charges = models.BooleanField()

    def __str__(self):
        return room_number

