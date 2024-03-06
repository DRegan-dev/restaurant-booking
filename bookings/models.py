from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    BOOKING_TIME_CHOICES = [
        ('18:00', "6:00PM"),
        ('19:00', "7:00PM"),
        ('20:00', "10:00PM"),
        ('21:00', "9:00PM"),
        ('22:00', "10:00PM")
    ]
    booking_time = models.DateTimeField(choices=BOOKING_TIME_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
