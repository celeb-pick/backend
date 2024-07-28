from django.db import models

class Celebrity(models.Model):
    name = models.CharField(max_length=20)
    profile_image_url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
