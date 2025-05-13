import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

temas_procurados = {}
def get_api(tema):
    """
        Faz uma requisição à API da NewsAPI para buscar notícias com base em um tema.
        Args:
            tema (str): O tema ou palavra-chave para buscar notícias (ex.: 'tecnologia').
        Returns:
            dict: Dados JSON retornados pela API contendo as notícias, se a requisição for bem-sucedida.
            tuple: ('Erro!!', Exception) se ocorrer um erro na requisição.
        Raises:
            requests.exceptions.RequestException: Erros relacionados à requisição HTTP, como conexão falha ou timeout.
        Note:
            A função usa a chave da API armazenada na variável de ambiente 'KEY_NEWS'.
            A linguagem das notícias é definida como 'pt' (português).
    """

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
            return data


    except requests.exceptions.RequestException as e:
        return 'Erro!!', e

    
def menu():
    """
        Exibe um menu de opções para o usuário e retorna a escolha.
        Returns:
            str: A opção digitada pelo usuário (ex.: '0', '1', '2').
    """


    print()
    linha()
    print("0 - Sair\n" \
          "1 - Ver Noticias\n" \
          "2 - Ver Histórico\n")
    linha()
    try:
        opcao = input('Digite a Opção que deseja: ')
        linha()
        return opcao
    except KeyboardInterrupt:
        print('\nPrograma Finalizado pelo Usuario!')
        exit()

def solicitar_noticia():

    """
        Solicita ao usuário um tema e quantidade de notícias, busca e exibe as notícias.
        Modifica o dicionário global 'temas_procurados' incrementando a contagem do tema procurado.
        Returns:
            None
        Raises:
            ValueError: Se a quantidade de notícias digitada não for um número inteiro válido.
            requests.exceptions.RequestException: Erros relacionados à requisição à API.
        Note:
            A quantidade de notícias é limitada a 10, e o tema é usado para buscar notícias via get_api().
    """


    while True:

        try:
            quantidade_noticia = int(input(f'Digite quantas noticias você deseja ver [max-10]: '))
            linha()

            if 1 <= quantidade_noticia <= 10:
                break
            else:
                print('Digite um valor entre 1-10')

        except ValueError:
            print('Entrada inválida! Digite um numero entre 1-10')
        except KeyboardInterrupt:
            print('\nPrograma Finalizado pelo Usuario!')
            exit()

    while True:

        try:
            tema = input('Digite o tema que deseja ver as noticias: ')
            linha()
            noticia = get_api(tema)

            if noticia['articles']:
                break
            else:
                print('Tema invalido ou não encontrado')

        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar notícias: {e}")
        
        except KeyboardInterrupt:
            print('\nPrograma Finalizado pelo Usuario!')
            exit()
            
    # Incrementa a contagem de vezes que o tema foi procurado no dicionário temas_procurados.
    # Usa .get(tema, 0) para retornar 0 se o tema não existir, evitando erros, e adiciona 1 ao contador.
    temas_procurados[tema] = temas_procurados.get(tema, 0) + 1

    for i in noticia['articles'][:quantidade_noticia]:
            print()
            print(f"Autor: {i['author']}")
            print(f"Título: {i['title']}")
            print(f"Texto: {i['description']}")
            print(f"Fonte: {i['url']}")


def mostrar_historico():
    """
        Exibe o histórico de temas procurados e suas respectivas contagens.
        Utiliza o dicionário global 'temas_procurados' para gerar uma lista de temas e contagens.
        Returns:
            None
        Note:
          Se nenhum tema foi procurado, exibe uma mensagem informativa.
            Os dados são exibidos como uma lista de dicionários contendo 'tema' e 'contagem'.
    """

    if not temas_procurados:
        print("Nenhum tema foi procurado ainda.")
    else:
        lista_temas = [{"tema": tema, "contagem": contagem} for tema, contagem in temas_procurados.items()]
        print("Temas procurados (como lista):")
        for item in lista_temas:
            print(f"'{item['tema']}': {item['contagem']} vez(es)")

def linha():
    """
    Exibe linhas decorativas para uma melhor visualização do usuario
    """
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
