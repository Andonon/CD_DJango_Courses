# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]