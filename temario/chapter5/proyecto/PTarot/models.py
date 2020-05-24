from django.db import models
from django.utils import timezone

# Create your models here.

class Carta(models.Model):
    """  Creamos la clase Carta """
    dia = models.IntegerField(default=0)
    mes = models.IntegerField(default=0)
    anyo = models.IntegerField(default=0)

    def __str__(self):
        return str(self.dia)+"/"+str(self.mes)+"/"+str(self.anyo)
    


class Usuario(models.Model):
    """ Creamos la clase Usuario """
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    GENERO = (
        ('FEMENINO','FEMENINO'),
        ('MASCULINO','MASCULINO')
    )
    sexo = models.CharField(max_length=50,choices=GENERO, default='MASCULINO')
    carta =  models.ForeignKey(Carta)

    def __str__(self):
        return self.nombre+", "+self.apellidos+", "+self.sexo+", "+str(self.carta)

