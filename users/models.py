from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxLengthValidator

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    MALE = "남성"
    FEMALE = "여성"
    GENDER_CHOICES = (
      (MALE, "남성"),
      (FEMALE, "여성"),
    )

    outfit_post_scraps = models.ManyToManyField("outfit_posts.OutfitPost", through="scraps.OutfitPostScrap", related_name="users")
    outfit_item_scraps = models.ManyToManyField("outfit_posts.OutfitItem", through="scraps.OutfitItemScrap", related_name="users")
    email = models.EmailField(unique=True, error_messages={'unique': "이미 존재하는 이메일 입니다."})
    nickname = models.CharField(
        max_length=6,
        unique=True,
        error_messages={"unique": "이미 존재하는 닉네임 입니다."},
      )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )
    profile_image = models.CharField(max_length=300, blank=True)
    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email