# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0006_auto_20170301_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
