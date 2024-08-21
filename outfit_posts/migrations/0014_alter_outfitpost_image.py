# Generated by Django 4.2.14 on 2024-08-21 16:07

import django.core.validators
from django.db import migrations, models
import outfit_posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit_posts', '0013_remove_outfitpost_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfitpost',
            name='image',
            field=models.ImageField(upload_to=outfit_posts.models.generate_filename, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'jfif', 'png', 'bmp', 'webp', 'tif', 'tiff'])]),
        ),
    ]
