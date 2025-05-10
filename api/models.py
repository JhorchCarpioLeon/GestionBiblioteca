
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField(blank=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    editorial = models.CharField(max_length=100, blank=True)
    numero_paginas = models.PositiveIntegerField(null=True, blank=True)
    idioma = models.CharField(max_length=30, default='Español')
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)
    resumen = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
