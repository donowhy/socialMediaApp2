# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialMedia', '0003_auto_20160706_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilephotos',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialMedia.profile'),
        ),
    ]