from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext



#def index(request):
    #return HttpResponse("<h1>Calculando carta de Tarot.</h1>")

def index(request):
    return render(request, 'tarot/index.html',{})

