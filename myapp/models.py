from django.db import models

class Project( models.Model ):
    '''
    Modelo que representa un proyecto
    '''
    name = models.CharField(max_length=50, help_text='Ingrese el nombre del projecto')

class Task( models.Model ):
    '''
    Modelo que representa una tarea de un proyecto 
    '''
    title = models.CharField(max_length=200, help_text='Ingrese el titulo de la tarea.')
    description = models.CharField(help_text='Ingrese la descripción de la tarea.')
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
