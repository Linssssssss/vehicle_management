# Generated by Django 4.2.1 on 2023-09-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_app', '0003_alter_fuel_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
