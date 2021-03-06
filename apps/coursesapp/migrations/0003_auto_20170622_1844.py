# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapp', '0002_descriptions'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Descriptions',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='description',
        ),
        migrations.AddField(
            model_name='courses',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courses',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
