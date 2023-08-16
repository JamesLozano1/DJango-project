from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about),
    path('holaMundo/<str:username>', views.holaMundo),
    path('multiplicacion/<int:numero>', views.multiplicacion),
    path('taks/<int:id>', views.taks),
    path('ProjectName/<str:name>', views.BuscarNombre),
    path('projects', views.projects, name='projects'),
    path('task', views.taks, name='tasks'),
    path('create_task', views.create_task, name='create_task'),
    path('create_project', views.create_project, name='create_project'),
    path('tasks_project/<int:project_id>', views.tasks_project),
]