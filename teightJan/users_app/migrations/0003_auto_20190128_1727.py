# Generated by Django 2.1.4 on 2019-01-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20190128_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author_model',
            name='git',
            field=models.URLField(blank=True, max_length=128),
        ),
    ]
