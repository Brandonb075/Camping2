from django.db import models

# Create your models here.

class Campista (models.Model):
    id=models.AutoField(primary_key=True)
    identificacion=models.CharField(max_length=10)
    nombre=models.CharField(max_length=100)
    correo=models.EmailField()
    telefono=models.CharField(max_length=12)
    direccion=models.TextField()
    def _str_(self):
        return self.nombre

class Reserva(models.Model):
    id=models.AutoField(primary_key=True)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    campista=models.ForeignKey(Campista, on_delete=models.CASCADE)
    alojamiento=models.CharField(max_length=50)
    numero_personas=models. CharField(max_length=2)
    Estado=models.CharField(max_length=50)
    observaciones=models.CharField(max_length=300)
    def _str_(self):
        return f"Reserva de {self.campista.nombre}({self.fecha_inicio}-{self.fecha_fin})"
