from django.db import models

class OutfitPostScrap(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    outfit_post = models.ForeignKey("outfit_posts.OutfitPost", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class OutfitItemScrap(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    outfit_item = models.ForeignKey("outfit_posts.OutfitItem", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
