import datetime
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

# Create your models here.


class Users(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    contrasenha = EncryptedCharField(max_length=255)
    es_administrador = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Companies(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Customers(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    company = models.ForeignKey(Companies, null=False, blank=False, on_delete = models.PROTECT)
    user = models.ForeignKey(Users, null=False, blank=False, on_delete = models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.nombre
    
    def cumpleanhos_actual(self):
        hoy = datetime.date.today()
        try:
            fecha = datetime.date(hoy.year, self.fecha_nacimiento.month , self.fecha_nacimiento.day)
        except Exception:
            # Se asume como unico caso el 29 de febrero de un año bisiesto
            print(f"Customer id={self.id} fecha_nacimiento={self.fecha_nacimiento}")
            fecha = datetime.date(hoy.year, 3 , 1)
        return fecha

    

class Interactions(models.Model):
    customer = models.ForeignKey(Customers, null=False, blank=False, on_delete = models.PROTECT)
    tipo = models.CharField(max_length=20)
    fecha_interaccion = models.DateTimeField()
