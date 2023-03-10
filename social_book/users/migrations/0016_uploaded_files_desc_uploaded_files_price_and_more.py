# Generated by Django 4.1.2 on 2023-02-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_uploaded_files_delete_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaded_files',
            name='desc',
            field=models.TextField(default='', max_length=1500),
        ),
        migrations.AddField(
            model_name='uploaded_files',
            name='price',
            field=models.IntegerField(default='1000'),
        ),
        migrations.AddField(
            model_name='uploaded_files',
            name='publish_year',
            field=models.CharField(default=' ', max_length=10),
        ),
        migrations.AddField(
            model_name='uploaded_files',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
    ]
