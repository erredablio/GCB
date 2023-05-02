# GCB

***

## Gerador de sorteios para compra de biscoitos

>O gerador é executado todos os dias às 0h.
>
>A cada execução, caso seja segunda-feira, é disparado um e-mail com a relação de todos >os próximos sorteados a levar os biscoitos.
>
>O sorteador da semana, 1 dia antes, recebe um e-mail para lembrá-lo que é a sua vez de levar os biscoitos.

***

## Stack

- #### Python - 3.8.10

- #### Django - 4.2

- #### Whitenoise - 6.4.0

- #### guinicorn - 20.1.0

- #### Django-crontab - 0.7.1

***

## Extras

- ### SECRET_KEY

> Está localizada em: */etc/secret_key.txt*

- ### CRON

> Está configurado como: * 0 * * * */usr/bin/python3 /home/ricwagner1/Projetos/GCB/manage.py crontab run 8397bc307ddf7b8f5d8060ebcbe5d5a9 # django-cronjobs for GCB_Django*

- ### gcb.services

> Foi criado um service para manter o serviço do gunicorn rodando em segundo plano, no seguinte caminho: */lib/systemd/system*
>
>*[unit]*\
>*Description=Executavel GCB*\
>*after=network.target*
>
>
>*[Service]*\
>*User=ricwagner1*\
>*WorkingDirectory=/home/ricwagner1/Projetos/GCB*\
>*ExecStart=/home/ricwagner1/.local/bin/gunicorn -c ./GCB_Django/conf/guniconf-config.py GCB_Django.wsgi*
>
>*[Install]*\
>*WantedBy=multi-user.target*
>
>\
>Após a criação do arquivo, foram executados os seguintes comandos para o correto registro do serviço:
>
>
> - *sudo systemctl daemon-reload*
> - *sudo systemctl enable gcb.service*
> - *sudo systemctl start gcb.service*
