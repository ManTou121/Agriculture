# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=32)),
                ('content', models.TextField(null=True)),
                ('create_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
