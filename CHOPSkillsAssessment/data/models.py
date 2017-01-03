from __future__ import unicode_literals
from django.db import models
#from django.forms import ModelForm

# Create your models here.

AVAILABLE_FLAG_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No')
    )

VOL_UNITS_CHOICES = (
    ('ul', 'microliter'),
    ('mg', 'milligram'),
    ('cubmm', 'cubic millimeter' ),
    ('ug','microgram' ),
    ('ml','milliliter' ),
    ('cubm','cubic meter' ),
    ('mm','Millimolar' ),
    ('off', 'off'),
    ('', '')
    )

class Aliquot(models.Model):
    aliquot_id= models.AutoField(primary_key = True)
    received_on = models.DateField()
    collected_on = models.DateField(blank = True)
    sample_type_code = models.CharField(max_length=5)
    secondary_sample_code = models.CharField(max_length=5, blank = True)
    sample_type = models.CharField(max_length=30)
    secondary_sample_type = models.CharField(max_length=30)
    full_sample_type_desc = models.TextField()
    origin_aliquot_desc = models.TextField(blank = True)
    tissue_type = models.TextField(blank = True)
    specimen_category = models.TextField(blank = True)
    volume_received = models.IntegerField(blank = True)
    volume_remaining = models.IntegerField(blank = True)
    vol_units = models.CharField(max_length=10, blank = True, default = '',
                                        choices = VOL_UNITS_CHOICES)
    alq_status = models.TextField(blank = True)
    available_flag = models.CharField(max_length=1, default = 'Y',
                                      choices = AVAILABLE_FLAG_CHOICES)


