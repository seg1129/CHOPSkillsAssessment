from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Aliquot(models.Model):
    aliquot_id= models.AutoField(primary_key = True)
    received_on = models.DateField()
    collected_on = models.DateField()
    sample_type_code = models.CharField(max_length=5)
    secondary_sample_code = models.CharField(max_length=5)
    sample_type = models.CharField(max_length=30)
    secondary_sample_type = models.CharField(max_length=30)
    full_sample_type_desc = models.TextField()
    origin_aliquot_desc = models.TextField()
    tissue_type = models.TextField()
    specimen_category = models.TextField()
    volume_received = models.IntegerField()
    volume_remaining = models.IntegerField()
    vol_units = models.CharField(max_length=3)
    alq_status = models.TextField()
    available_flag = models.CharField(max_length=1)


