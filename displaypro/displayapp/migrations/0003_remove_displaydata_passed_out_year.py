# Generated by Django 5.1.1 on 2024-10-01 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displayapp', '0002_rename_locationn_displaydata_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='displaydata',
            name='passed_out_year',
        ),
    ]