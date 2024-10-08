# Generated by Django 4.2.14 on 2024-07-28 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('outfit_posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutfitItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('IDOL', '아이돌'), ('MODEL', '모델'), ('SINGER', '가수'), ('ACTOR', '배우'), ('INFLUENCER', '인플루언서'), ('OTHERS', '기타')], max_length=10)),
                ('name', models.CharField(max_length=60)),
                ('purchase_link', models.CharField(blank=True, max_length=300)),
                ('image_url', models.CharField(max_length=300)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
            ],
        ),
    ]
