# Generated by Django 4.0.1 on 2022-03-03 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0004_alter_photo_classification_alter_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='classification',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
    ]
