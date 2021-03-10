from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User


class Author(models.Model):
    author_first_name = models.CharField(max_length=100,null=False)
    author_middle_name = models.CharField(max_length=100,null=False)
    author_last_name = models.CharField(max_length=100,null=False)

class Podcasts(models.Model):
    podcast_name = models.CharField(max_length=1000,null=False)
    podcast_tags = models.CharField(max_length=100,null=True)
    author_id = models.ForeignKey(Author,on_delete=models.CASCADE)

class Shows(models.Model):
    podcast_id = models.ForeignKey(Podcasts,on_delete=models.CASCADE)
    show_title = models.CharField(max_length=100,null=False)
    show_watched = models.BooleanField(default=False)
    show_notes = models.TextField()
    show_link = models.TextField()

class CustomUser(AbstractBaseUser):
    pass