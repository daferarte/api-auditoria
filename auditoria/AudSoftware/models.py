__author__ = "Daniel Arteaga"
__copyright__ = "Copyright 2022, Auditoria"
__credits__ = ["Daniel Arteaga"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Daniel Arteaga"
__email__ = "dfarteaga@unicesmag.edu.co"
__status__ = "Test"

from django.db import models
import jsonfield

# Create your models here.
"""
    @Class AuditoriaSoftware
    metodo que crea el ORM de la base de datos para auditoria de software
    Charfield es equivalente a varchar
    DateTime es equivalente a date
    BigIntegerField es equivalente a big int
    jsonfield campo equivalente json
    para mas ayuda consultar la documentacion de Django
"""
class AuditoriaSoftware(models.Model):
    modulo = models.CharField(max_length=100, verbose_name='Modulo')
    accion = models.CharField(max_length=6, verbose_name='Operación')
    aplicativo = models.CharField(max_length=10, verbose_name='Aplicativo')
    consulta = jsonfield.JSONField()
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    usuario = jsonfield.JSONField()
    

    class Meta:
        verbose_name = 'Auditoria Software'
        verbose_name_plural = 'Auditorias Software'

    def __str__(self):
        return self.modulo

"""
    @Class AuditoriaMoodle
    metodo que crea el ORM de la base de datos para auditoria de moodle
    Charfield es equivalente a varchar
    DateTime es equivalente a date
    BigIntegerField es equivalente a big int
    jsonfield campo equivalente json
    para mas ayuda consultar la documentacion de Django
"""
class AuditoriaMoodle(models.Model):
    aplicativo = models.CharField(max_length=10, verbose_name='Aplicativo')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    usuario = jsonfield.JSONField()
    

    class Meta:
        verbose_name = 'Auditoria moodle'
        verbose_name_plural = 'Auditorias moodle'

    def __str__(self):
        return self.usuario