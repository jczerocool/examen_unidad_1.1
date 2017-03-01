"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from libros import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^listadelibros/$', views.lista_libros, name='lista_libros'),
    url(r'^detalle/(?P<object_id>\d+)/$', views.detalle_libro, name='detalle_libro'),
    url(r'^agregar_libro/$', views.agregar_libro, name='nuevo_libro'),
    url(r'^detalle_slug/(?P<slug>[\w-]+)/$', views.detalle_slug, name='detalle_slug'),

]
