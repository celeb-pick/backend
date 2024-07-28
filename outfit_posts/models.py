from django.db import models

class OutfitPost(models.Model):
	MALE = "MALE"
	FEMALE = "FEMALE"
	UNISEX = "UNISEX"
	GENDER_CHOICES = (
		(MALE, "남성"),
		(FEMALE, "여성"),
		(UNISEX, "공용"),
	)

	celebrity_id = models.ForeignKey("celebrities.Celebrity", on_delete=models.CASCADE)
	created_by = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	gender = models.CharField(
		max_length=10,
		choices=GENDER_CHOICES,
	)
	image_url = models.CharField(max_length=300)

# class OutfitItem(models.Model):
# 	pass

# class OutfitPostItem(models.Model):
# 	pass