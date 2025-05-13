import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

noticias = []
def get_api(tema):


    url = f'https://newsapi.org/v2/everything'
    api_news = os.getenv('KEY_NEWS')

    headers = {
        'Authorization' : api_news
    }

    params = {
        'q': tema,
        'language': 'pt' 
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        

        if response.status_code == 200:
            data = response.json()

            if not data:
                return 'Tema invalido ou não encontrado'
            
            return data

        else:
            return 'Tema invalido'
    except requests.exceptions.RequestException as e:
        return 'Erro!!', e

    
def menu():
    print()
    linha()
    print("0 - Sair\n" \
          "1 - Ver Noticias\n" \
          "2 - Ver Histórico\n")
    linha()
    opcao = input('Digite a Opção que deseja: ')
    linha()
    return opcao

def solicitar_noticia():

    quantidade_noticia = int(input(f'Digite quantas noticias você deseja ver [max-10]: '))
    linha()
    if quantidade_noticia <= 10:
        tema = input('Digite o tema que deseja ver as noticias: ')
        linha()
        noticia = get_api(tema)

        if not noticia:
            print('Tema invalido ou não encontrado')

        
        noticias.append(tema)
        print(noticia)
        for i in noticia['articles'][:quantidade_noticia]:
            print()
            print(f"Author: {i['author']}")
            print(f"Titulo: {i['title']}")
            print(f"Texto: {i['description']}")
            print(f"Fonte: {i['url']}")


def mostrar_historico():

    if not noticias:
        print('Nenhum tema procurado')
    else:
        print('Temas solicitados')
        for i in len(noticias):
            print(i)

def linha():
    print('=-'*20)





while True:
    opcao = menu()

    if opcao == '0':
        print('Até mais!!')
        break
    elif opcao == '1':
        solicitar_noticia()
    elif opcao == '2':
        mostrar_historico()
