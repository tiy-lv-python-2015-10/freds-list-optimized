from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.title)


class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category)

    def __str__(self):
        return "{}".format(self.title)


class State(models.Model):
    name = models.CharField(max_length=15)
    short = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.short)


class City(models.Model):
    state = models.ForeignKey(State)
    name = models.CharField(max_length=35)

    def __str__(self):
        return "{}".format(self.name)


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User)
    subcategory = models.ForeignKey(SubCategory)
    phone = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    location = models.ForeignKey(City)
    favorited = models.ManyToManyField(User, through='Favorite', related_name='favorite_post')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.title)


class Image(models.Model):
    image = models.ImageField(upload_to="media/",null=True, blank=True)
    posting = models.ForeignKey(Post, related_name="images")


class Favorite(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    favorited_at = models.DateTimeField(auto_now_add=True)