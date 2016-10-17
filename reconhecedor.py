#Fluxo principal de código
comandos = []
#variaveis = []

nomeArquivo = input('Nome do arquivo: ')

arquivo = open(nomeArquivo, 'r')

for line in arquivo.readLines():
    # A primeira palavra de cada frase é enviada em lowercase para o reconhecedor
    # De acordo com o retorno do reconhecedor será decido qual ação tomar em seguida
    primeiraPalavra = line.split()[0]
    retorno = reconhecer(primeiraPalavra.lower())

    if retorno == 1:
        reconhecerVar(line)
    else if retorno == 2:
        reconhecerWrite(line)

# Função responsável por interpretar a primeira palavra da linha
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
    else if palavra[0] != "'" and palavra[0] != '"': #caso seja uma variavel já criada
        return 6
    else: #Erro
        return 0

def reconhecerVar(linha):

    linha = linha.replace('write', '', 1)
    linha = linha.strip()

    if (linha[0] == "'" or linha[0] == '"'):
        #Erro

    else if (int(linha[0]) or float(linha[0])):
        #Erro

def reconhecerWrite(linha):
    #Remove a palavra Write da frase
    #Limpa espaços em branco no começo ou final da linha
    linha = linha.replace('write', '', 1)
    linha = linha.strip()
    
    #Verifica se abriu parenteses
    if linha[0] == '(':
        #verifica se abriu aspas simples ou duplas
        linha = linha.replace('(','',1)
        linha = linha.strip()

        if (linha[0] == '"' or linha[0] == "'"):
            
            #Guardar texto em variável

            #Verificar se fechou aspas simples ou duplas

            #Verificar se fechou parenteses


def reconhecerRead(linha):
    #SEMPRE DAR STRIP()
    #Remover a palavra Read da frase
    #Verificar abertura de parenteses
        #Verificar se nao tem aspas simples ou duplas
            #verificar se nao começa com numero
                #verificar se fechou parenteses
                    #verificar se colocou ponto e virgula
                        #adicionar ao vetor comandos

def reconhecerIf(linha):


def reconhecerFor(linha):


# Função responsável por executar os comandos
# Interpretar a linha e executar o comando respectivo
# Por enquanto esse método só vai verificar que comando foi encontrado ou se aconteceu erro;
def executar: