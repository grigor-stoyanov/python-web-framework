# Generated by Django 4.0.2 on 2022-02-28 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
