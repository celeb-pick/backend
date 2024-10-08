# Generated by Django 4.2.14 on 2024-07-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0002_alter_celebrity_options_celebrity_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebrity',
            name='category',
            field=models.CharField(choices=[('IDOL', '아이돌'), ('MODEL', '모델'), ('SINGER', '가수'), ('ACTOR', '배우'), ('INFLUENCER', '인플루언서'), ('OTHERS', '기타')], default='아이돌', max_length=10),
            preserve_default=False,
        ),
    ]
