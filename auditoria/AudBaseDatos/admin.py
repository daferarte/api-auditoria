__author__ = "Daniel Arteaga"
__copyright__ = "Copyright 2022, Auditoria"
__credits__ = ["Daniel Arteaga"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Daniel Arteaga"
__email__ = "dfarteaga@unicesmag.edu.co"
__status__ = "Test"

from django.contrib import admin
from .models import AuditoriaBaseDatos

# Register your models here.

"""
@class AudBaseDatosAdmin
Clase que permite la manipulacion, los filtros y demas en el administrador de djando
"""
class AudBaseDatosAdmin(admin.ModelAdmin):
    readonly_fields = ('UpdateDate',)
    search_fields = ('UserName','UpdateDate','OldValue','NewValue','Operation','TableName')
     # list_filter=('visible',)
    list_display = ('TableName', 'UpdateDate')
    ordering = ('-UpdateDate', )

# Register your models here.
admin.site.register(AuditoriaBaseDatos, AudBaseDatosAdmin)