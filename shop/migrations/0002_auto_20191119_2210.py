# Generated by Django 2.2.7 on 2019-11-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelips',
            name='calling_code',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='modelips',
            name='country_flag',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='modelips',
            name='country_name',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
