from django.db import models
from django.contrib.postgres.fields import ArrayField


class Fan(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, default=None, null=True, blank=True)
    token = models.CharField(max_length=256, default=None)
    password = models.CharField(max_length=256, null=True, blank=True)

class Artist(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256, default=None)
    token = models.CharField(max_length=256, default=None)
    password = models.CharField(max_length=256, default=None)

class ArtistProfile(models.Model):
    photo = models.FileField(null=True, blank=True, default=None)
    description = models.TextField()
    social_links = ArrayField(models.CharField(max_length=256), blank=True)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE, related_name='artist_profile', null=True, blank=True)

class Release(models.Model):
    title = models.CharField(max_length=256)
    urls = ArrayField(models.CharField(max_length=256), blank=True, null=True)
    slug = models.CharField(max_length=256, null=True, blank=True)
    photo = models.FileField(null=True, blank=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE, related_name='release', null=True, blank=True)

    @property
    def artist_name(self):
        return self.artist.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    url = models.TextField()
    embed_code = models.CharField(max_length=256, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE, related_name='product', null=True, blank=True)

    @property
    def artist_name(self):
        return self.artist.name
