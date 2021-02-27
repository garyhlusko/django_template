from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author_first_name = Models.CharField(null=True)
    author_middle_name = Models.CharField(null=True)
    author_last_name = Models.CharField(null=True)

class Podcasts(models.Model):
    podcast_name = Models.CharField(null=False)
    podcast_tags = Models.CharField(null=True)
    author_id = Models.ForeignKey(Author)

class Shows(models.Model):
    podcast_id = Models.ForeignKey(Podcast)
    show_title = Models.CharField(null=False)
    show_watched = Models.Boolean()
    show_notes = Models.TextField()
    show_link = Modlels.TextField()

class CustomUser(AbstractBaseUser):
    pass