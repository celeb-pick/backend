from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    MALE = "MALE"
    FEMALE = "FEMALE"
    GENDER_CHOICES = (
      (MALE, "남성"),
      (FEMALE, "여성"),
    )

    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=6)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )
    profile_image_url = models.CharField(max_length=300, blank=True)
    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email