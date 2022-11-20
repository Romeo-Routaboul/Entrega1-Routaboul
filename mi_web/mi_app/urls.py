from django.urls import path
from mi_app.views import*

urlpatterns = [
    path("inicio/", inicio, name='inicio'),
    path("registro_vendedor/", registro_vendedor, name='registro_vendedor'),
    path("registro_automoviles/", registro_automoviles, name='registro_automoviles'),
    path("registro_clientes/", registro_clientes, name='registro_clientes'),
    path("busqueda_automoviles/", busqueda_automoviles, name='busqueda_automoviles'),
    path("resultado_busqueda_automoviles/", resultado_busqueda_automoviles, name='resultado_busqueda_automoviles'),


]