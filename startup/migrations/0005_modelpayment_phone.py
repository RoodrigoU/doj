# Generated by Django 2.2.7 on 2019-11-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0004_modelpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelpayment',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]