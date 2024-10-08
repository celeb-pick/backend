from django.db import models
from django.dispatch import receiver
from django.core.validators import MinLengthValidator, FileExtensionValidator
import uuid
import os


def generate_outfit_post_image_filename(value, filename):
    extension = os.path.splitext(value.image.name)[1]
    return f"outfit-post/{str(uuid.uuid4())}{extension}"


class OutfitPost(models.Model):
	MALE = "남성"
	FEMALE = "여성"
	UNISEX = "공용"
	GENDER_CHOICES = (
		(MALE, "남성"),
		(FEMALE, "여성"),
		(UNISEX, "공용"),
	)	

	items = models.ManyToManyField("outfit_posts.OutfitItem", through="outfit_posts.OutfitPostItems")
	celebrity = models.ForeignKey("celebrities.Celebrity", related_name="outfit_posts", on_delete=models.CASCADE)
	creator = models.ForeignKey("users.CustomUser", related_name="outfit_posts", on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=40, validators=[MinLengthValidator(4)])
	created_at = models.DateTimeField(auto_now_add=True)
	gender = models.CharField(
		max_length=10,
		choices=GENDER_CHOICES,
	)
	image = models.ImageField(
		upload_to=generate_outfit_post_image_filename,
		validators=[FileExtensionValidator([
			"jpg",
			"jpeg",
			"jfif",
			"png",
			"bmp",
			"webp",
			"tif",
			"tiff",
		])]
	)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return self.title


@receiver(models.signals.pre_delete, sender=OutfitPost)
def outfit_post_auto_delete_file_on_delete(sender, instance, **kwargs):
		instance.image.delete()


class OutfitPostItems(models.Model):
    outfit_post = models.ForeignKey("outfit_posts.OutfitPost", on_delete=models.CASCADE)
    outfit_item = models.ForeignKey("outfit_posts.OutfitItem", on_delete=models.CASCADE)


def generate_outfit_item_image_filename(value, filename):
    extension = os.path.splitext(value.image.name)[1]
    return f"outfit-item/{str(uuid.uuid4())}{extension}"


class OutfitItem(models.Model):
	TOP = "상의"
	BOTTOM = "하의"
	OUTERWEAR = "아우터"
	SHOES = "신발"
	BAG = "가방"
	ACCESSORY = "악세사리"
	OTHERS = "기타"
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
	name = models.CharField(max_length=40)
	purchase_link = models.CharField(max_length=300, blank=True)
	image = models.ImageField(
		upload_to=generate_outfit_item_image_filename,
		validators=[FileExtensionValidator([
			"jpg",
			"jpeg",
			"jfif",
			"png",
			"bmp",
			"webp",
			"tif",
			"tiff",
		])]
	)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return self.name


@receiver(models.signals.pre_delete, sender=OutfitItem)
def outfit_item_auto_delete_file_on_delete(sender, instance, **kwargs):
		instance.image.delete()