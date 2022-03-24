# Generated by Django 4.0.2 on 2022-03-17 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.URLField(default='http://asd.bg'),
            preserve_default=False,
        ),
    ]