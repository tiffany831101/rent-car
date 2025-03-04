# Generated by Django 5.0.4 on 2024-05-03 09:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_vehicles_types_vender_vehicles_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Violation_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('fee', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('actual_return_time', models.DateTimeField(null=True)),
                ('actual_return_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='rent.city')),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rent.order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField(default=0)),
                ('invoice_no', models.CharField(max_length=100)),
                ('payment_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_record', to='rent.payment_type')),
                ('rent_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='rent.rent')),
            ],
        ),
        migrations.CreateModel(
            name='Violation_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='violate_records', to='rent.order')),
                ('Violation_types_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='violate_records', to='rent.violation_types')),
            ],
        ),
        migrations.CreateModel(
            name='Violation_name_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_time', models.DateTimeField()),
                ('ended_time', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='violate_records', to=settings.AUTH_USER_MODEL)),
                ('violate_record_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.violation_records')),
            ],
        ),
    ]
