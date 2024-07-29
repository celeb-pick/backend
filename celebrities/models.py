from django.db import models

class Celebrity(models.Model):
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

    name = models.CharField(max_length=20)
    category = models.CharField(
		max_length=10,
		choices=CATEGORY_CHOICES,
	)
    profile_image_url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
