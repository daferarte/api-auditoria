__author__ = "Daniel Arteaga"
__copyright__ = "Copyright 2022, Auditoria"
__credits__ = ["Daniel Arteaga"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Daniel Arteaga"
__email__ = "dfarteaga@unicesmag.edu.co"
__status__ = "Test"

from rest_framework import serializers
from .models import AuditoriaSoftware

"""
    @Class AuditoriaSoftwareSerializers
    metodo que permiten que datos complejos, como conjuntos de consultas e instancias de modelos, 
    se conviertan en tipos de datos nativos de Python que luego se pueden representar fácilmente en 
    JSON, XML u otros tipos de contenido.
"""

class AuditoriaSoftwareSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaSoftware  
        exclude = ['is_removed', 'created', 'modified']