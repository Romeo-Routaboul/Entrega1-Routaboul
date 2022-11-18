from django.db import models

# Create your models here.

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField() 

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()