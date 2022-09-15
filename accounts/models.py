from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='male')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'email']