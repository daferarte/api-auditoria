__author__ = "Daniel Arteaga"
__copyright__ = "Copyright 2022, Auditoria"
__credits__ = ["Daniel Arteaga"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Daniel Arteaga"
__email__ = "dfarteaga@unicesmag.edu.co"
__status__ = "Test"

from django.contrib import admin
from .models import AuditoriaMoodle, AuditoriaSoftware

# Register your models here.

"""
@class AudBaseDatosAdmin
Clase que permite la manipulacion, los filtros y demas en el administrador de djando
"""
class AudSoftwareAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    search_fields = ('usuario','fecha','aplicativo','accion','modulo','consulta')
     # list_filter=('visible',)
    list_display = ('aplicativo','usuario', 'fecha')
    ordering = ('-fecha', )

class AudMoodleAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    search_fields = ('aplicativo','usuario','fecha')
     # list_filter=('visible',)
    list_display = ('usuario','aplicativo', 'fecha')
    ordering = ('-fecha', )

# Register your models here.
admin.site.register(AuditoriaSoftware, AuditoriaMoodle, AudSoftwareAdmin, AudMoodleAdmin)