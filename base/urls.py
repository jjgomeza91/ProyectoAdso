"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from base.views import principal
from base.views import clientes
from base.views import ventas
from base.views import devoluciones
from base.views import bodegas
from base.views import compras
from base.views import productos
from base.views import proveedores
from base.views import roles
from base.views import usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',principal,name="index"),
    path('clientes/', clientes, name='clientes'),
    path('ventas/', ventas, name='ventas'),
    path('devoluciones/', devoluciones, name='devoluciones'),
    path('bodegas/', bodegas, name='bodegas'),
    path('compras/', compras, name='compras'),
    path('productos/', productos, name='productos'),
    path('proveedores/', proveedores, name='proveedores'),
    path('roles/', roles, name='roles'),
    path('usuarios/', usuarios, name='usuarios'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
