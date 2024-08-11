# Generated by Django 4.2.14 on 2024-08-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': '이미 존재하는 이메일 입니다.'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('남성', '남성'), ('여성', '여성')], max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 존재하는 닉네임 입니다.'}, max_length=6, unique=True),
        ),
    ]
