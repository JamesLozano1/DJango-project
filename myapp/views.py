from django.shortcuts import render
from django.http import HttpResponse

def holaMundo( request ):
    return HttpResponse('Hello world!')

def about( request ):
    return HttpResponse('<h1>About us</h1>')

def products( request ):
    return HttpResponse('<h1>products</h1>')