from django.db import models


# Create your models here.


class Proyecto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    completada = models.BooleanField(default=False)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.titulo} - {self.proyecto.nombre}"
