from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q

import requests


class Agency(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    contact_number = models.TextField()
    email = models.TextField()
    logo = models.ImageField(upload_to='agency_logos/', null=True, blank=True)

    def __str__(self):
        return self.name

class User(AbstractUser):

    title = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    agency = models.ForeignKey(Agency, on_delete=models.SET_NULL, null=True, blank=True)
    is_agency_admin = models.BooleanField(default=False)
    request_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    contact_number = models.TextField()
    description = models.TextField()

    # USERNAME_FIELD = email
    REQUIRED_FIELDS = []
    

    def __str__(self):
        return self.username




class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=50)  # House, Apartment, Condo
    location = models.TextField()
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    

    listing_date = models.DateField()
    status = models.CharField(max_length=50, default='available')  # Available, Pending, Sold

    # def __str__(self):
    #     return self.title

class PropertyFeatures(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    parking = models.BooleanField(default=False)
    floor_size = models.CharField(max_length=255)
    erf_size = models.CharField(max_length=255)
    garages = models.CharField(max_length=255)
    pet_friendly = models.CharField(max_length=255)
    pool  = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.property


class HouseImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='property-images/')
    is_main = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.property

class HouseVideos(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    videos = models.FileField(upload_to='property-videos/')
    is_main = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.property
