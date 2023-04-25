from django.shortcuts import redirect, render
from datetime import datetime, timedelta
from django.core.mail import send_mail
from .models import Pessoa
import random


# Create your views here.

def home(request):
    pessoas = Pessoa.objects.filter(status = True, escolhido = True).order_by('data')
    atual = Pessoa.objects.filter(status = True, escolhido = True, data__exact=datetime.now()).order_by('data')[:1]
    proximo = Pessoa.objects.filter(status = True, escolhido = True, data__gt=datetime.now()).order_by('data')[:1]
    controle_gerador = Pessoa.objects.filter(status = True, escolhido = False).count()

    context = {'pessoas': pessoas, 'atual': atual, 'proximo': proximo, 'controle_gerador': controle_gerador}
    return render(request, 'home.html', context)

def sortear(request):
    i = 0
    x = 7    
    qtd = Pessoa.objects.filter(status = True).count()

    if Pessoa.objects.filter(status = True, escolhido = True, data__lt=datetime.now()).order_by('-data')[:1]:
        escolhido = Pessoa.objects.filter(status = True, escolhido = True, data__lt=datetime.now()).first().pk
        maior_data = Pessoa.objects.filter(status = True, escolhido = True).order_by('-data').first().data

        Pessoa.objects.filter(pk = escolhido).update(data = maior_data + timedelta(days=x))

    if Pessoa.objects.filter(status = True, escolhido = True, data=datetime.now()).order_by('-data')[:1]:
        escolhido = Pessoa.objects.filter(status = True, escolhido = True, data=datetime.now()).first().pk
        maior_data = Pessoa.objects.filter(status = True, escolhido = True).order_by('-data').first().data

        Pessoa.objects.filter(pk = escolhido).update(data = maior_data + timedelta(days=x))
    
    if Pessoa.objects.filter(status = True, escolhido = False).count() > 0:
        i = 0
        x = 7
        for i in range(qtd):
            ninguem = Pessoa.objects.filter(status = True, escolhido = False)
            escolhido = random.choice(ninguem).pk
            Pessoa.objects.filter(pk=escolhido).update(status = True, escolhido = True, data = datetime.now() + timedelta(days=x))    
            x += 7
            i += 1

    if int(datetime.now().weekday()) == 7:
        i = 0 
        qtd_ativos = Pessoa.objects.filter(status = True, escolhido = True).count()
        escolhido = Pessoa.objects.filter(status = True, escolhido = True).values_list('email')
        for i in range(qtd_ativos):
            subject = 'Relatório Biscoito - '+ datetime.now().strftime("%d/%m/%Y") +''
            from_email = 'ricwagner1@gmail.com'
            message = 'a'
            recipient_list = escolhido[i]
            html_message = '<b>Relação das próximas semanas</b>'
            send_mail(
                subject=subject,
                message=message, 
                from_email=from_email, 
                recipient_list=recipient_list, 
                html_message=html_message,
                fail_silently=False)
            i += 1

    if Pessoa.objects.filter(status = True, escolhido = True, data__exact=datetime.now() + timedelta(days=1)).count() > 0:
        atual = Pessoa.objects.filter(status = True, escolhido = True, data__exact=datetime.now() + timedelta(days=1)).values_list('email')

        subject = 'Você deverá levar os biscoitos AMANHÃ'
        from_email = 'ricwagner1@gmail.com'
        message = 'a'
        recipient_list = atual[0]
        html_message = '<b>Levar amanhã os biscoitos</b>'
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False)
    return redirect('../')


def limpar(request):
    Pessoa.objects.filter(escolhido = True).update(escolhido = False)

    return redirect('../')