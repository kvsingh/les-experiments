# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-17 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aritst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=200)),
                ('artist_wordcloud', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
