import requests

def executar():
    response = requests.get('https://gcb-production.up.railway.app/sortear/')
    return response