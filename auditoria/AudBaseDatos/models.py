__author__ = "Daniel Arteaga"
__copyright__ = "Copyright 2022, Auditoria"
__credits__ = ["Daniel Arteaga"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Daniel Arteaga"
__email__ = "dfarteaga@unicesmag.edu.co"
__status__ = "Test"

from django.db import models

# Creación de modelos
"""
    @Class AuditoriaBaseDatos
    metodo que crea el ORM de la base de datos para auditoria
    Charfield es equivalente a varchar
    DateTime es equivalente a date
    BigIntegerField es equivalente a big int
    para mas ayuda consultar la documentacion de Django
"""
class AuditoriaBaseDatos(models.Model):
    TableName = models.CharField(max_length=100, verbose_name='Nombre Tabla')
    Operation = models.CharField(max_length=1, verbose_name='Operación')
    OldValue =  models.CharField(max_length=255, verbose_name='Antiguos valores', blank=True, null=True)
    NewValue = models.CharField(max_length=255, verbose_name='Nuevos valores', blank=True, null=True)
    UpdateDate = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    UserName = models.CharField(max_length=70, verbose_name='Usuario')
    idtabla = models.BigIntegerField(verbose_name='idTabla')
    

    class Meta:
        verbose_name = 'Auditoria Base de Datos'
        verbose_name_plural = 'Auditorias Bases de Datos'

    def __str__(self):
        return self.name