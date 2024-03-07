from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    party_size = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2, message="Value must be at least 2"),
            MaxValueValidator(6, message="Value must be at most 6")],
        default=2
    )
    
    booking_date = models.DateField(default=timezone.now)
    booking_time = models.TimeField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    special_requests = models.TextField(null=True)

    approved = models.BooleanField(default=False)

    def validate_future_date(value):
        if value < timezone.now().date():
            raise ValidationError("Selected date must be today or in the future")
