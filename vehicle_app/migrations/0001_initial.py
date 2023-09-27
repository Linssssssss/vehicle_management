# Generated by Django 4.2.1 on 2023-08-28 09:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('Driver_license_number', models.CharField(max_length=50)),
                ('LNO_expiry_date', models.DateField()),
                ('categories_approved', models.CharField(max_length=254)),
                ('training', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plate_no', models.CharField(max_length=20, unique=True)),
                ('vehicle_make', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('telephone', models.IntegerField()),
                ('Insuarance_start_date', models.DateField()),
                ('Insuarance_expiry_date', models.DateField()),
                ('last_inspection_date', models.DateField()),
                ('next_inspection_date', models.DateField()),
                ('last_service_distance', models.IntegerField()),
                ('Distance_remaining', models.IntegerField(default=5000)),
                ('odometer', models.IntegerField(default=0)),
                ('expected_efficiency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Daily_vehicle_tracking_distance', models.IntegerField()),
                ('Overspeeding', models.IntegerField()),
                ('JMP_daily_distance', models.IntegerField()),
                ('Driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_app.driver')),
                ('Vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_app.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Start_odometer_reading', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('Stop_odometer_reading', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('Round_trip_distance', models.IntegerField(default=0)),
                ('vehicle_condition', models.CharField(max_length=50)),
                ('initial_JMP', models.TimeField()),
                ('final_JMP', models.TimeField()),
                ('start_trip', models.CharField(max_length=100)),
                ('stop_trip', models.CharField(max_length=254)),
                ('destination', models.CharField(max_length=300)),
                ('passengers', models.CharField(max_length=254)),
                ('Approver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle_app.aprover')),
                ('Driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle_app.driver')),
                ('Vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle_app.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('current_odometer_reading', models.IntegerField()),
                ('total_distance_from_previous_fueling', models.IntegerField()),
                ('Liters_taken', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('receipt', models.ImageField(upload_to='')),
                ('effiency', models.IntegerField()),
                ('variation', models.IntegerField()),
                ('Driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle_app.driver')),
                ('Vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_app.vehicle')),
            ],
        ),
    ]
