# Generated by Django 3.0.5 on 2020-04-22 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('release_date', models.DateTimeField()),
                ('show_date', models.DateTimeField()),
                ('tickets', models.CharField(choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6')], default='', max_length=100)),
                ('seatNo', models.CharField(max_length=100)),
                ('theater', models.CharField(max_length=100)),
                ('theater_location', models.TextField()),
                ('cast', models.CharField(max_length=100)),
                ('language', models.CharField(choices=[('Telugu', 'Telugu'), ('Hindi', 'Hindi'), ('English', 'English'), ('Malayalam', 'Malayalam'), ('kannada', 'kannada')], default='Telugu', max_length=13)),
                ('movie_type', models.CharField(choices=[('2d', '2D'), ('3d', '3D'), ('imax2d', 'IMAX 2D'), ('imax3d', 'IMAX 3D'), ('4dx', '4DX'), ('4dx3d', '4DX 3D'), ('mx4d', 'MX4D')], default='2d', max_length=7)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]