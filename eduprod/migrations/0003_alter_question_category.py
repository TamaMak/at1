# Generated by Django 5.0.2 on 2024-03-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0002_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(default='Europe', max_length=50),
        ),
    ]
