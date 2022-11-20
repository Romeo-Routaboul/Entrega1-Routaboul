from django.http import HttpResponse

def inicio(request):
    return HttpResponse('para probar la pagina dirigirse a "coder/inicio/"')