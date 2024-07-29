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
	celebrity = models.ForeignKey("celebrities.Celebrity", related_name="outfit_posts", on_delete=models.CASCADE)
	creator = models.ForeignKey("users.CustomUser", related_name="outfit_posts", on_delete=models.SET_NULL, null=True)
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
	TOP = "TOP"
	BOTTOM = "BOTTOM"
	OUTERWEAR = "OUTERWEAR"
	SHOES = "SHOES"
	BAG = "BAG"
	ACCESSORY = "ACCESSORY"
	OTHERS = "OTHERS"
	CATEGORY_CHOICES = (
		(TOP, "상의"),
		(BOTTOM, "하의"),
		(OUTERWEAR, "아우터"),
		(SHOES, "신발"),
		(BAG, "가방"),
		(ACCESSORY, "악세사리"),
		(OTHERS, "기타"),
	)

	brand = models.ForeignKey("brands.Brand", related_name="outfit_items", on_delete=models.CASCADE)
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
