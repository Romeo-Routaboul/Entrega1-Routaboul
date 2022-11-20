from django.shortcuts import render
from mi_app.models import*



# Create your views here.

def inicio(request):
    return render(request, "mi_app/inicio.html")

def registro_vendedor(request):
    if request.method == "POST":
        nombre_vendedor = request.POST["nombre"]
        telefono_vendedor = request.POST["telefono"]
      
        vendedor = Vendedor(nombre=nombre_vendedor, telefono= telefono_vendedor)
        vendedor.save()

    return render(request, "mi_app/registro_vendedor.html")

def registro_automoviles(request):
    if request.method == "POST":
        marca_auto = request.POST["marca"]
        modelo_auto = request.POST["modelo"]
        precio_auto = request.POST["precio"]
      
        autos = Auto(marca=marca_auto, modelo= modelo_auto, precio= precio_auto)
        autos.save()
    return render(request, "mi_app/registro_automoviles.html")

def registro_clientes(request):
    if request.method == "POST":
        nombre_cliente = request.POST["nombre"]
        telefono_cliente = request.POST["telefono"]
      
        cliente = Cliente(nombre=nombre_cliente, telefono= telefono_cliente)
        cliente.save()

    return render(request, "mi_app/registro_clientes.html")

def busqueda_automoviles(request):

    return render(request, "mi_app/busqueda_automoviles.html")

def resultado_busqueda_automoviles(request):
    marca_autos = request.GET["marca_autos"]

    autos = Auto.objects.filter(marca__icontains = marca_autos)
    return render (request, "mi_app/resultado_busqueda_autos.html", {"autos":autos})
