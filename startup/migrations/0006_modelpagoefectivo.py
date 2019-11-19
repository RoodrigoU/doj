# Generated by Django 2.2.7 on 2019-11-17 23:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0005_modelpayment_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPagoEfectivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('object', models.CharField(blank=True, default='', max_length=250)),
                ('create_data_time', models.IntegerField()),
                ('expiration_date_time', models.IntegerField()),
                ('orde_id', models.CharField(blank=True, default='', max_length=250)),
                ('order_number', models.CharField(blank=True, default='', max_length=250)),
                ('amount', models.FloatField(blank=True, default=0.0)),
                ('payment_code', models.CharField(blank=True, default='', max_length=250)),
                ('currency_code', models.CharField(blank=True, default='', max_length=250)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('state', models.CharField(blank=True, default='', max_length=250)),
                ('total_fee', models.CharField(blank=True, default='', max_length=250)),
                ('net_amount', models.CharField(blank=True, default='', max_length=250)),
                ('fee_details', models.CharField(blank=True, default='', max_length=250)),
                ('updated_at', models.CharField(blank=True, default='', max_length=250)),
                ('paid_at', models.CharField(blank=True, default='', max_length=250)),
                ('available_on', models.CharField(blank=True, default='', max_length=250)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('name', models.CharField(blank=True, default='', max_length=400)),
                ('lastname', models.CharField(blank=True, default='', max_length=400)),
                ('phone', models.CharField(blank=True, default='', max_length=400)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
            ],
        ),
    ]