#Fluxo principal de código
def main:
    comandos = []
    variaveis = []

    nomeArquivo = input('Nome do arquivo: ')

    arquivo = open(nomeArquivo, 'r')

    for line in arquivo.readLines():
        # A primeira palavra de cada frase é enviada para o reconhecedor
        # De acordo com o retorno do reconhecedor será decido qual ação tomar em seguida
        primeiraPalavra = line.split()[0]
        retorno = reconhecer(primeiraPalavra)


# Função responsável por interpretar a frase
# 1.Reconhecer palavras-chaves/reservadas
# 2.Reconhecer Strings
# 3.Reconhecer variáveis
# 4.Retornar valor a ser armazenado no array COMANDOS
def reconhecer(palavra):
    if palavra == 'var':
        return 1
    else if palavra == 'write':
        return 2
    else if palavra == 'read':
        return 3
    else if palavra == 'if':
        return 4
    else if palavra == 'for':
        return 5
    else if palavra[0] != "'" && palavra[0] != '"': #caso seja uma variavel já criada
        return 6
    else: #Erro
        return 0

def reconhecerWrite:


def reconhecerRead:


def reconhecerVar:


def reconhecerIf:


def reconhecerFor:


# Função responsável por executar os comandos
# Interpretar a linha e executar o comando respectivo
# Por enquanto esse método só vai verificar que comando foi encontrado ou se aconteceu erro;
def executar: