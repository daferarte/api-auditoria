from django.contrib import admin
from .models import AuditoriaBaseDatos

# Register your models here.

class AudBaseDatosAdmin(admin.ModelAdmin):
    readonly_fields = ('UpdateDate',)
    search_fields = ('UserName','UpdateDate','OldValue','NewValue','Operation','TableName')
     # list_filter=('visible',)
    list_display = ('TableName', 'UpdateDate')
    ordering = ('-UpdateDate', )

# Register your models here.
admin.site.register(AuditoriaBaseDatos, AudBaseDatosAdmin)