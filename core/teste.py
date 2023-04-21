    # i = 2
    # x = 7    
    # pessoas_nao_escolhidas = Pessoa.objects.filter(escolhido=False)
    # qtd = Pessoa.objects.count()
    # while (qtd > i):
    #     id = random.choice(pessoas_nao_escolhidas).pk
    #     Pessoa.objects.filter(pk=id).update(escolhido = True, data = datetime.now() + timedelta(days=x))        
    #     x += 7
    #     i += 1 

from datetime import datetime, timedelta
import random

x = 7
z = ['Símio A', 'Símio B', 'Símio C', 'Símio D']
random.shuffle(z)

while z:
    sorteado = z.pop()
    data = datetime.now() + timedelta(days=x)
    print(data, sorteado)
    x += 7
