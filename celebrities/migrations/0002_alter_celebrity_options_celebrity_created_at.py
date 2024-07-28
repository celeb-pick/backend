# Generated by Django 4.2.14 on 2024-07-28 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celebrity',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='celebrity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
