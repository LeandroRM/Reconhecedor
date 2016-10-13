#Fluxo principal de código
def main:
    comandos = []
    variaveis = []

    nomeArquivo = input('Nome do arquivo: ')

    arquivo = open(nomeArquivo, 'r')

    for line in arquivo.readLines():
        # Cada frase é enviada para o reconhecedor
        # De acordo com o retorno do reconhecedor será decido qual ação tomar em seguida
        retorno = reconhecer(line)


# Função responsável por interpretar a frase
# 1.Reconhecer palavras-chaves/reservadas
# 2.Reconhecer Strings
# 3.Reconhecer variáveis
# 4.Retornar valor a ser armazenado no array COMANDOS
def reconhecer:
    

def reconhecerWrite:


def reconhecerRead:


def reconhecerVar:


def reconhecerIf:


def reconhecerFor:


# Função responsável por executar os comandos
# Interpretar a linha e executar o comando respectivo
# Por enquanto esse método só vai verificar que comando foi encontrado ou se aconteceu erro;
def executar: