# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-26 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("misago_theming", "0003_auto_20181226_1841")]

    operations = [
        migrations.RemoveField(model_name="theme", name="license"),
        migrations.AddField(
            model_name="theme",
            name="version",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
