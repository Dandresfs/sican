from __future__ import unicode_literals
from productos.models import Diplomado
from region.models import Region
from django.db import models
from radicados.models import Radicado
from formacion.models import Formador, Grupos
from usuarios.models import User

# Create your models here.
class Area(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __unicode__(self):
        return self.nombre

class Grado(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __unicode__(self):
        return self.nombre

class Beneficiario(models.Model):
    usuario = models.ForeignKey(User,blank=True,null=True)
    vigencia = models.CharField(max_length=100)

    diplomado = models.ForeignKey(Diplomado,related_name='diplomado_beneficiario')
    region = models.ForeignKey(Region,related_name='region_beneficiario')
    radicado_text = models.CharField(max_length=1000,blank=True)
    radicado = models.ForeignKey(Radicado,blank=True,null=True,related_name='radicado_beneficiario')

    departamento_text = models.CharField(max_length=1000,blank=True,null=True)
    secretaria_text = models.CharField(max_length=1000,blank=True,null=True)
    dane_ie_text = models.CharField(max_length=1000,blank=True,null=True)
    ie_text = models.CharField(max_length=1000,blank=True,null=True)
    dane_sede_text = models.CharField(max_length=1000,blank=True,null=True)
    sede_text = models.CharField(max_length=1000,blank=True,null=True)
    municipio_text = models.CharField(max_length=1000,blank=True,null=True)
    zona_text = models.CharField(max_length=1000,blank=True,null=True)

    formador = models.ForeignKey(Formador,related_name='formador_beneficiario')
    grupo = models.ForeignKey(Grupos,related_name='grupo_beneficiario')
    ruta = models.CharField(max_length=100,blank=True)
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    cedula = models.BigIntegerField(unique=True)
    correo = models.EmailField(max_length=100,blank=True,null=True)
    telefono_fijo = models.CharField(max_length=100,blank=True,null=True)
    telefono_celular = models.CharField(max_length=100,blank=True,null=True)
    area = models.ForeignKey(Area,related_name='area_beneficiario',blank=True,null=True)
    grado = models.ForeignKey(Grado,related_name='grado_beneficiario',blank=True,null=True)
    genero = models.CharField(max_length=100,blank=True,null=True)
    estado = models.CharField(max_length=100,blank=True,null=True)
    usuario_colombia_aprende = models.CharField(max_length=100,blank=True)

    diploma = models.FileField(upload_to='Diplomas',blank=True,null=True)
    ip_descarga = models.GenericIPAddressField(max_length=100,blank=True,null=True)
    fecha_descarga = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
        return str(self.cedula) + ' - ' + self.nombres + ' ' + self.apellidos

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos

    def get_grupo(self):
        return self.ruta + '-' + self.grupo.nombre

    def get_diploma_url(self):
        try:
            url = self.diploma.url
        except:
            url = ""
        return url

    def get_diploma_url_rest(self):
        try:
            url = self.diploma.url
        except:
            url = None
        return url

    def diplomado_name(self):
        return self.diplomado.nombre


class BeneficiarioPendiente(models.Model):
    diplomado = models.ForeignKey(Diplomado,related_name='diplomado_beneficiariopendiente')
    cedula = models.BigIntegerField(unique=True)

    def __unicode__(self):
        return str(self.cedula)

class CargaMasiva(models.Model):
    usuario = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now_add=True)
    archivo = models.FileField(upload_to='Carga Masiva/Archivo')
    resultado = models.FileField(upload_to='Carga Masiva/Resultado',blank=True,null=True)
    estado = models.CharField(max_length=100,default='Procesando...')

    def get_archivo_url(self):
        try:
            url = self.archivo.url
        except:
            url = ""
        return url

    def get_resultado_url(self):
        try:
            url = self.resultado.url
        except:
            url = ""
        return url