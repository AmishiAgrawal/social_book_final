# Generated by Django 4.1.2 on 2023-02-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_customuser_expdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='expdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]