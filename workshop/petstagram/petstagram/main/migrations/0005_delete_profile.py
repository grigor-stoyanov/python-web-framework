# Generated by Django 4.0.2 on 2022-03-17 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_petphoto_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]