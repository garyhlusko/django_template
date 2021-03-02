from django.db import models
rom django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User


class Author(models.Model):
    author_first_name = models.CharField(null=True)
    author_middle_name = models.CharField(null=True)
    author_last_name = models.CharField(null=True)

class Podcasts(models.Model):
    podcast_name = models.CharField(null=False)
    podcast_tags = models.CharField(null=True)
    author_id = models.ForeignKey(Author,on_delete=models.SET_NULL)

class Shows(models.Model):
    podcast_id = models.ForeignKey(Podcasts,on_delete=models.SET_NULL)
    show_title = models.CharField(null=False)
    show_watched = models.Boolean(default=False)
    show_notes = models.TextField()
    show_link = models.TextField()

class CustomUser(AbstractBaseUser):
    pass