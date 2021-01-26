# Generated by Django 3.1 on 2021-01-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0003_auto_20210126_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('emailid', models.EmailField(default='', max_length=254)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
    ]