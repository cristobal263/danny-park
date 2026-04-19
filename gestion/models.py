from django.db import models
from django.utils import timezone

class Plaza(models.Model):
    # Identificador único (ej: plaza-A-14)
    identificador = models.CharField(max_length=15, unique=True) 
    ocupada = models.BooleanField(default=False)
    patente = models.CharField(max_length=10, blank=True, null=True)
    hora_ingreso = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.identificador

class RegistroCobro(models.Model):
    # Historial para la planilla diaria
    identificador_plaza = models.CharField(max_length=20)
    patente = models.CharField(max_length=10)
    hora_ingreso = models.DateTimeField()
    hora_salida = models.DateTimeField(auto_now_add=True)
    minutos = models.IntegerField()
    total_pagado = models.IntegerField()

    def __str__(self):
        return f"{self.patente} - ${self.total_pagado}"