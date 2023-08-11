from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('holaMundo/<str:username>', views.holaMundo),
    path('multiplicacion/<int:numero>', views.multiplicacion),
    path('projects', views.projects),
    path('taks/<int:id>', views.taks),
]