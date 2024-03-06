from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    booking_time = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
