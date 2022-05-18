from django.db import models

# Create your models here.
class AuditoriaBaseDatos(models.Model):
    TableName = models.CharField(max_length=100, verbose_name='Nombre Tabla')
    Operation = models.CharField(max_length=1, verbose_name='Operación')
    OldValue =  models.CharField(max_length=255, verbose_name='Antiguos valores', blank=True)
    NewValue = models.CharField(max_length=255, verbose_name='Nuevos valores', blank=True)
    UpdateDate = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    UserName = models.CharField(max_length=70, verbose_name='Usuario')
    idtabla = models.BigIntegerField(verbose_name='idTabla')
    

    class Meta:
        verbose_name = 'Auditoria Base de Datos'
        verbose_name_plural = 'Auditorias Bases de Datos'

    def __str__(self):
        return self.name