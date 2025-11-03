from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira pagina Django!</h1>")

def call(request):
    return HttpResponse("<h1>Chamada por aqui.</h1>")