from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICE = (
    ('All', 'All'),
    ('Kids', 'Kids')
)

MOVIE_CHOICE = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile')


class Profile(models.Model):
    name = models.CharField(max_length=200)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICE)
    uuid = models.UUIDField(default=uuid.uuid4)


class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICE)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=18, choices=AGE_CHOICE)


class Video(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to='movies')
