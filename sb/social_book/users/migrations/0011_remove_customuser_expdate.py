# Generated by Django 4.1.2 on 2023-02-10 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_customuser_ccnumber_remove_customuser_cctype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='expdate',
        ),
    ]