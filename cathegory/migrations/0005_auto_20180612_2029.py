# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-12 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cathegory', '0004_auto_20180605_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='cathegory.Topic'),
        ),
    ]