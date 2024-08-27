# Generated by Django 4.2.14 on 2024-08-27 03:25

import celebrities.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0004_alter_celebrity_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celebrity',
            name='profile_image_url',
        ),
        migrations.AddField(
            model_name='celebrity',
            name='profile_image',
            field=models.ImageField(default='a', upload_to=celebrities.models.generate_profile_image_filename, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'jfif', 'png', 'bmp', 'webp', 'tif', 'tiff'])]),
            preserve_default=False,
        ),
    ]
