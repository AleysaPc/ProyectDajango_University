from django.db import models

# Create your models here.
#Model Template View MTV
#ORM Object Relational M

class Curso (models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)#como maximo 50 caracteres
    creditos = models.PositiveSmallIntegerField()


