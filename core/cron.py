import requests

def executar():
    response = requests.get('http://localhost:8000/sortear/')
    return response