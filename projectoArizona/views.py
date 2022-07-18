from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 

def cursoD(request):
    print('Hola mundo')
    return render(request,"Inicio.html")


