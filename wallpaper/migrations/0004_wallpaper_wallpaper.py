# Generated by Django 3.0.1 on 2020-05-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0003_wallpaper_heart'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallpaper',
            name='Wallpaper',
            field=models.BooleanField(default=False),
        ),
    ]
