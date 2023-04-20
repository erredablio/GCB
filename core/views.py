from django.shortcuts import redirect, render
from datetime import datetime, timedelta
from .models import Pessoa
import random
import operator

# Create your views here.

def home(request):
    pessoas = Pessoa.objects.filter(escolhido=True).order_by('data')
    proximo = Pessoa.objects.filter(escolhido=True).order_by('data')[:1]

    context = {'pessoas': pessoas, 'proximo': proximo}
    return render(request, 'home.html', context)

def sortear(request):
    i = 0
    x = 7    
    qtd = Pessoa.objects.count()
    for i in range(qtd):
        ninguem = Pessoa.objects.filter(escolhido = False)
        escolhido = random.choice(ninguem).pk
        Pessoa.objects.filter(pk=escolhido).update(escolhido = True, data = datetime.now() + timedelta(days=x))    
        x += 7
        i += 1    
    return redirect('../')


def limpar(request):
    Pessoa.objects.filter(escolhido=True).update(escolhido=False)

    return redirect('../')