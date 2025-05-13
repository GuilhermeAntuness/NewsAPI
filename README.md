# InfoNewsBR

**Versão:** 1.0.0  
**Autor:** Guilherme Antunes  
**Descrição:** Um script em Python que permite buscar e exibir notícias em português com base em temas definidos pelo usuário, utilizando a API da NewsAPI.

## Sobre o Projeto

O *InfoNewsBR* é uma ferramenta simples desenvolvida em Python que permite ao usuário pesquisar notícias em português de acordo com um tema de interesse. O programa exibe até 10 notícias por vez, incluindo autor, título, descrição e link da fonte, e mantém um histórico dos temas procurados com a contagem de buscas. Ele utiliza a biblioteca `requests` para interagir com a NewsAPI e `python-dotenv` para gerenciar a chave da API de forma segura.

## Funcionalidades

- Buscar notícias em português com base em um tema escolhido.
- Limitar a quantidade de notícias exibidas (máximo de 10).
- Armazenar e exibir o histórico de temas procurados com suas respectivas contagens.
- Interface de menu simples para navegar entre opções.
- Tratamento de erros para conexões falhas ou temas inválidos.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados antes de executar o projeto:

- **Python 3.9 ou superior**
- Bibliotecas Python:
  - `requests`
  - `python-dotenv`

Você pode instalar as dependências usando o comando:

```bash
pip install requests python-dotenv