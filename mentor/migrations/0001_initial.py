# Generated by Django 2.2.7 on 2019-11-22 01:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('taller_name', models.CharField(blank=True, default='', max_length=250)),
                ('Nombre', models.CharField(blank=True, default='', max_length=250)),
                ('Apellido', models.CharField(blank=True, default='', max_length=250)),
                ('url_alumno', models.CharField(blank=True, default='', max_length=500)),
                ('file_certificate', models.CharField(blank=True, default='', max_length=250)),
            ],
        ),
    ]