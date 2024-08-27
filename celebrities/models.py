from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
import os

def generate_profile_image_filename(value, filename):
    extension = os.path.splitext(value.profile_image.name)[1]
    return f"celebrity/{str(uuid.uuid4())}{extension}"

class Celebrity(models.Model):
    IDOL = "아이돌"
    MODEL = "모델"
    SINGER = "가수"
    ACTOR = "배우"
    INFLUENCER = "인플루언서"
    OTHERS = "기타"
    CATEGORY_CHOICES = (
		(IDOL, "아이돌"),
		(MODEL, "모델"),
		(SINGER, "가수"),
		(ACTOR, "배우"),
		(INFLUENCER, "인플루언서"),
		(OTHERS, "기타"),
	)

    name = models.CharField(max_length=20)
    category = models.CharField(
		max_length=10,
		choices=CATEGORY_CHOICES,
	)
    profile_image = models.ImageField(
		upload_to=generate_profile_image_filename,
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
