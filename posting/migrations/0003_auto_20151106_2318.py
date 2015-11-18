# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0002_auto_20151106_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('short', models.CharField(null=True, blank=True, max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='posting.State'),
        ),
    ]
