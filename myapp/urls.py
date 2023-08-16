from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('holaMundo/<str:username>', views.holaMundo),
    path('multiplicacion/<int:numero>', views.multiplicacion),
    path('projects', views.projects),
    path('task', views.taks),
    path('taks/<int:id>', views.taks),
    path('ProjectName/<str:name>', views.BuscarNombre),
    path('create_task', views.create_task),
    path('create_project', views.create_project),
]