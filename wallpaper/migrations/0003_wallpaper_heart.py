# Generated by Django 3.0.1 on 2020-04-29 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0002_auto_20200429_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallpaper',
            name='heart',
            field=models.IntegerField(default=0),
        ),
    ]
