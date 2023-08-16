from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, createNewProyect

def index( request ):
    title = "Django Project!!"
    return render(request, 'index.html',{
        'title':title
    })

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
    # return JsonResponse(projects, safe=False)
    title = "Project: Este es un titulo desde views"
    return render(request, 'projects.html', {
        'title':title,
        'projects':projects
    })


#Listado de Tarea
# def taks( request, id ):
#     # task = Task.objects.get(id=id)
#     # task = get_object_or_404(Task, id=id)
#     # return HttpResponse("<h1>Taks: %s</h1>" % task.title)
#     return render(request, 'task.html')

def taks( request ):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse("<h1>Taks: %s</h1>" % task.title)
    title = "Task: Este es un titulo desde views"
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'title': title,
        'tasks':tasks
    })


def BuscarNombre( request, name ):
    # project = Project.objects.get(name=name)
    nombre = get_object_or_404(Project, name=name)
    return HttpResponse('<h1>Se ha encontrado el Projecto %s</h1>' % nombre)

def create_task( request ):
    if request.method == 'GET':    
        return render( request, 'create_task.html', {
            'form':CreateNewTask()
        })
    else: 
        title = request.POST['title']
        description = request.POST['description']
        project_id = 1
        Task.objects.create(title=title, description=description, project_id=project_id)
        return redirect('/task')

def create_project( request ):
    if request.method == 'GET':    
        return render( request, 'create_project.html', {
            'form':createNewProyect(),
        })
    else: 
        name = request.POST['name']
        Project.objects.create(name=name)
        return redirect('/projects')
    
        
# //HECHO CREAR UNA VISTA QUE RESIBA UN NUMBERO ENTERO QUE VENGA COMO PARAMETRO COMO URL LE SUME 100 Y LO MULTIPLIQUE POR 2
# buscar un projecto por el nombre 