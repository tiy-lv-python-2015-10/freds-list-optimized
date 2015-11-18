# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0003_auto_20151106_2318'),
        ('users', '0002_auto_20151106_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
