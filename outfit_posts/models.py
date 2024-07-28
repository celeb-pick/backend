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

	items = models.ManyToManyField("outfit_posts.OutfitItem")
	celebrity_id = models.ForeignKey("celebrities.Celebrity", on_delete=models.CASCADE)
	created_by = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	gender = models.CharField(
		max_length=10,
		choices=GENDER_CHOICES,
	)
	image_url = models.CharField(max_length=300)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return self.title

class OutfitItem(models.Model):
	IDOL = "IDOL"
	MODEL = "MODEL"
	SINGER = "SINGER"
	ACTOR = "ACTOR"
	INFLUENCER = "INFLUENCER"
	OTHERS = "OTHERS"
	CATEGORY_CHOICES = (
		(IDOL, "아이돌"),
		(MODEL, "모델"),
		(SINGER, "가수"),
		(ACTOR, "배우"),
		(INFLUENCER, "인플루언서"),
		(OTHERS, "기타"),
	)

	brand_id = models.ForeignKey("brands.Brand", on_delete=models.CASCADE)
	category = models.CharField(
		max_length=10,
		choices=CATEGORY_CHOICES,
	)
	name = models.CharField(max_length=60)
	purchase_link = models.CharField(max_length=300, blank=True)
	image_url = models.CharField(max_length=300)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return self.name
