from django.db import models

class Celebrity(models.Model):
    name = models.CharField(max_length=20)
    profile_image_url = models.CharField(max_length=300)
