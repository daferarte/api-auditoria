__author__ = "Daniel Arteaga"
__copyright__ = "Copyright 2022, Auditoria"
__credits__ = ["Daniel Arteaga"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Daniel Arteaga"
__email__ = "dfarteaga@unicesmag.edu.co"
__status__ = "Test"

"""auditoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
Manejo de URLS de todo el proyecto incluye las app creadas dentro del proyecto
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('aud1t0r/', admin.site.urls),
    path('', include('AudBaseDatos.urls')),
]

# ruta imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
