# Generated by Django 5.0.2 on 2024-03-30 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Score',
        ),
    ]
