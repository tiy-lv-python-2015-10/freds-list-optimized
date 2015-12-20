# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posting', '0003_auto_20151106_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('favorited_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='posting.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/', null=True, blank=True)),
                ('posting', models.ForeignKey(to='posting.Post', related_name='images')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='favorited',
            field=models.ManyToManyField(through='posting.Favorite', to=settings.AUTH_USER_MODEL, related_name='favorite_post'),
        ),
    ]
