import uuid

from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100)


class TourDifficulty(models.Model):
    name = models.CharField(max_length=32)


class TourFormat(models.Model):
    name = models.CharField(max_length=32)


class Tour(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField()
    format = models.ForeignKey("TourFormat", on_delete=models.SET_NULL)
    difficulty = models.ForeignKey("TourDifficulty", on_delete=models.SET_NULL)


class Attachments(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    record = models.ManyToManyField(Tour.id)


class UserTours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
