# Generated by Django 4.2.14 on 2024-07-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit_posts', '0005_alter_outfititem_brand_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfititem',
            name='category',
            field=models.CharField(choices=[('TOP', '상의'), ('BOTTOM', '하의'), ('OUTERWEAR', '아우터'), ('SHOES', '신발'), ('BAG', '가방'), ('ACCESSORY', '악세사리'), ('OTHERS', '기타')], max_length=10),
        ),
    ]
