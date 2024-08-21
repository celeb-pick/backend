# Generated by Django 4.2.14 on 2024-08-21 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit_posts', '0010_rename_outfititem_id_outfitpostitems_outfit_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfitpost',
            name='title',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
