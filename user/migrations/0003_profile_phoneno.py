# Generated by Django 3.0.5 on 2020-04-25 19:34

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_profile_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phoneNo',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
