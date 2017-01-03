# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliquot',
            name='alq_status',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='available_flag',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='collected_on',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='origin_aliquot_desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='secondary_sample_code',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='specimen_category',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='tissue_type',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='vol_units',
            field=models.CharField(blank=True, choices=[('ul', 'microliter'), ('mg', 'milligram'), ('cubmm', 'cubic millimeter'), ('ug', 'microgram'), ('ml', 'milliliter'), ('cubm', 'cubic meter'), ('mm', 'Millimolar'), ('off', 'off'), ('', '')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='volume_received',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='volume_remaining',
            field=models.IntegerField(blank=True),
        ),
    ]