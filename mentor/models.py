from django.db import models
from django.utils import timezone

# Create your models here.

class ModelAlumno(models.Model):
    time_create = models.DateTimeField(default=timezone.now, blank=True)
    url_alumno = models.CharField(max_length=500, default='', unique=True)
    file_certificate = models.CharField(max_length=250, default='', blank=True)
    taller_name = models.CharField(max_length=250, default='', blank=True)
    nombre = models.CharField(max_length=250, default='', blank=True)
    apellido = models.CharField(max_length=250, default='', blank=True)

    def __str__(self):
        return self.url_alumno
