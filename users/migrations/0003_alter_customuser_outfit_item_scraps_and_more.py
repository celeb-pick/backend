# Generated by Django 4.2.14 on 2024-07-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit_posts', '0005_alter_outfititem_brand_id_and_more'),
        ('scraps', '0003_alter_outfititemscrap_outfit_item_and_more'),
        ('users', '0002_customuser_outfit_item_scraps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='outfit_item_scraps',
            field=models.ManyToManyField(related_name='users', through='scraps.OutfitItemScrap', to='outfit_posts.outfititem'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='outfit_post_scraps',
            field=models.ManyToManyField(related_name='users', through='scraps.OutfitPostScrap', to='outfit_posts.outfitpost'),
        ),
    ]
