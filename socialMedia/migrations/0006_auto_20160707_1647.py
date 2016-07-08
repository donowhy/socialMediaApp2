# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialMedia', '0005_imageupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='wallPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=500)),
                ('postReceiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postSender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallpost_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ImageUpload',
        ),
        migrations.AlterField(
            model_name='profilephotos',
            name='picLocation',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]