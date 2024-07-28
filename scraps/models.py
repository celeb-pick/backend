from django.db import models

class OutfitPostScrap(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    outfit_post = models.ForeignKey("outfit_posts.OutfitPost", related_name="scraps", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

class OutfitItemScrap(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    outfit_item = models.ForeignKey("outfit_posts.OutfitItem", related_name="scraps", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
