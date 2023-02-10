# Generated by Django 4.1.2 on 2023-02-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_customuser_credit_num_customuser_ccnumber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ccnumber',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='cctype',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.AddField(
            model_name='customuser',
            name='credit_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, default='SOME STRING', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cvc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='expdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='public_visibility',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.CharField(blank=True, default='SOME STRING', max_length=500, null=True),
        ),
    ]
