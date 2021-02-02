# Generated by Django 3.1.5 on 2021-01-30 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0022_auto_20210131_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booked_turf_id',
            new_name='booked_turf_name',
        ),
        migrations.AlterField(
            model_name='booking',
            name='endTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='num_5v5',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=1, verbose_name='Number Of Turfs'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='startTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Start Time'),
        ),
        migrations.AlterField(
            model_name='turf_list',
            name='address',
            field=models.CharField(default='', max_length=500, verbose_name='Turf Address'),
        ),
        migrations.AlterField(
            model_name='turf_list',
            name='events',
            field=models.CharField(default='', max_length=500, verbose_name='Upcoming Events'),
        ),
        migrations.AlterField(
            model_name='turf_list',
            name='image',
            field=models.ImageField(default='', upload_to='../media', verbose_name='Turf Image'),
        ),
        migrations.AlterField(
            model_name='turf_list',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Turf Name'),
        ),
        migrations.AlterField(
            model_name='turf_list',
            name='num_5v5_turfs',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=1, verbose_name='Number Of Turfs [5v5 Size]'),
        ),
        migrations.AlterField(
            model_name='turf_list',
            name='price_per_hour_5v5_weekdays',
            field=models.IntegerField(default=500, verbose_name='Price per Hour [WEEKDAYS]'),
        ),
        migrations.AlterField(
            model_name='turf_list',
            name='price_per_hour_5v5_weekends',
            field=models.IntegerField(default=700, verbose_name='Price per Hour [WEEKENDS]'),
        ),
    ]