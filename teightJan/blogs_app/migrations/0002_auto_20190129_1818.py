# Generated by Django 2.1.4 on 2019-01-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='body_edited',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post_model',
            name='modified_on',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='post_model',
            name='published_on',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='post_model',
            name='title_edited',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
