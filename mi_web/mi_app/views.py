from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "mi_app/inicio.html")
    