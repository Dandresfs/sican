from __future__ import unicode_literals

from django.db import models
from departamentos.models import Departamento
from municipios.models import Municipio
from radicados.models import Radicado

# Create your models here.
class DocentesMinEducacion(models.Model):
    cedula = models.BigIntegerField()
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100,blank=True)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100,blank=True)
    cargo = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100,blank=True)
    telefono_fijo = models.BigIntegerField(blank=True)
    telefono_celular = models.BigIntegerField(blank=True)
    departamento = models.ForeignKey(Departamento,blank=True)
    municipio = models.ForeignKey(Municipio,blank=True)
    radicado = models.ForeignKey(Radicado,blank=True)

    class Meta:
        ordering = ['primer_apellido']

    def __unicode__(self):
        return ("%s %s %s %s") % (self.primer_nombre,self.segundo_nombre,self.primer_apellido, self.segundo_apellido)