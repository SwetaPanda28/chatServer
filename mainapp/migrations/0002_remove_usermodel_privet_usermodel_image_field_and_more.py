# Generated by Django 4.0 on 2021-12-16 18:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='privet',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='image_field',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='masterpassword',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='private',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='public',
            field=models.CharField(default='', max_length=100),
        ),
    ]
