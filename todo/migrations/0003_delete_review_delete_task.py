# Generated by Django 5.1.1 on 2024-09-07 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
