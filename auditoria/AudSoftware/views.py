__author__ = "Daniel Arteaga"
__copyright__ = "Copyright 2022, Auditoria"
__credits__ = ["Daniel Arteaga"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Daniel Arteaga"
__email__ = "dfarteaga@unicesmag.edu.co"
__status__ = "Test"


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AuditoriaSoftwareSerializers
from .models import AuditoriaSoftware
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

"""
    @Class AudSoft_APYView
    y el método POST que permitirá guardar registros en la base de datos. 
"""
class AudSoft_APYView(APIView):

    def post(self, request, format=None):
        serializer = AuditoriaSoftwareSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    @Class AudSoft_APYView_List
    clase responderá a la petición GET que traera el listado de nuestra auditoria
"""
class AudSoft_APYView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        auditoria = AuditoriaSoftware.objects.all()
        serializer = AuditoriaSoftwareSerializers(auditoria, many=True)
        return Response(serializer.data)
    
"""
    @Class AudSoft_APIView_Detail
    nos permitira hacer métodos referentes a nuestra auditoria
    métodos para consultar una sola auditoria, editar o eliminar una auditoria con un id determinado o una primary key
"""
class AudSoft_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return AuditoriaSoftware.objects.get(pk=pk)
        except AuditoriaSoftware.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        auditoria = self.get_object(pk)
        serializer = AuditoriaSoftwareSerializers(auditoria)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        auditoria = self.get_object(pk)
        serializer = AuditoriaSoftwareSerializers(auditoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        auditoria = self.get_object(pk)
        auditoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)