from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

def index( request ):
    return HttpResponse('<h1>Index page</h1>')

def holaMundo( request, username ):
    print(username)
    return HttpResponse('Hello %s' % username)

def about( request ):
    return HttpResponse('<h1>About us</h1>')

def products( request ):
    return HttpResponse('<h1>products</h1>')

def multiplicacion( request, numero ):
    num = numero + 100
    resultado = num * 2
    return HttpResponse('La respuesta de (%s + 100) * 2 es: %s' % (numero,resultado))

#Listado de todos los projectos 
def projects( request ):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

#Listado de Tarea
def taks( request, id ):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse("<h1>Taks: %s</h1>" % task.title)

def BuscarNombre( request, name ):
    return
# //HECHO CREAR UNA VISTA QUE RESIBA UN NUMBERO ENTERO QUE VENGA COMO PARAMETRO COMO URL LE SUME 100 Y LO MULTIPLIQUE POR 2
# buscar un projecto por el nombre 