# Generated by Django 3.2.19 on 2023-06-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='イメージ画像'),
        ),
    ]
