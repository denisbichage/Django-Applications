# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.
def increment_id():
  last_booking = Studentinfo.objects.all().order_by('sid').last()
  if not last_booking:
    return 'ETL' + str(datetime.date.today().year) + '0000'
  if str(datetime.date.today().year) != last_booking.sid[3:7]:
    return 'ETL' + str(datetime.date.today().year) + '0000'
  booking_id = last_booking.sid
  booking_int = int(booking_id[7:11])
  new_booking_int = booking_int + 1
  new_booking_id = 'ETL' + str(str(datetime.date.today().year))  + str(new_booking_int).zfill(4)
  return new_booking_id

class Studentinfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=6)
    adhaar = models.CharField(max_length=12)
    mobile_no = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=50)
    parent_mobile = models.CharField(max_length=10)
    address_l1 = models.CharField(max_length=100)
    address_l2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    guardian_name = models.CharField(max_length=50)
    guardian_mobile = models.CharField(max_length=10)
    institution_name = models.CharField(max_length=30)
    hod_name = models.CharField(max_length=30)
    hod_mobile = models.CharField(max_length=10)
    registration_date = models.DateTimeField(auto_now=True)
    sid = models.CharField(max_length = 20, default = increment_id, editable=False, primary_key=True)
    def __str__(self):
        return self.sid
