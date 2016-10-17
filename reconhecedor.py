def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def isVariavelValid(var):
    if var[0] == "'" or var[0] == '"':
        return False
    elif isNumber(var[0]):
        return False
    else:
        return True

# Função responsável por interpretar a primeira palavra da linha
# 1.Reconhecer palavras-chaves/reservadas
# 2.Reconhecer Strings
# 3.Reconhecer variáveis
# 4.Retornar valor a ser armazenado no array COMANDOS
def reconhecer(palavra):
    if palavra == 'var':
        return 1
    elif palavra == 'write':
        return 2
    elif palavra == 'read':
        return 3
    elif palavra == 'if':
        return 4
    elif palavra == 'for':
        return 5
    elif palavra[0] != "'" and palavra[0] != '"': #caso seja uma variavel já criada
        return 6
    else: #Erro
        return 0

def reconhecerVar(linha):
    linha = linha.replace('var', '', 1)
    linha = linha.strip()

    if (linha[len(linha) - 1] == ';'):
        nomeVar = linha.split()[0]
        nomeVar = linha.split('=')[0]
    
        if isVariavelValid(nomeVar):            
            linha = linha.replace(nomeVar, '', 1)
            comandos.append('Declarou a variavel: ' + nomeVar)


def reconhecerWrite(linha):
    #Remove a palavra Write da frase
    #Limpa espaços em branco no começo ou final da linha
    linha = linha.replace('write', '', 1)
    linha = linha.strip()

    sTexto = "Erro no Write"

    #Verifica se utilizou ponto e virgula no final 
    if linha[len(linha) - 1] == ';':
        #Remove o ponto e virgula
        linha = linha[0:len(linha) - 1]
        linha = linha.strip()

        #Verifica se colocou os parenteses
        if linha[0] == '(' and linha[len(linha) - 1] == ')':
            #Remove os parenteses
            linha = linha[1:len(linha) - 1]
            linha = linha.strip()

            #Verifica se adicionou as aspas 
            if (linha[0] == '"' or linha[0] == "'") and (linha[len(linha) - 1] == '"' or linha[len(linha) - 1] == "'"):
                #Remove as aspas
                linha = linha[1:len(linha) - 1]
                linha = linha.strip()

                #Guardar texto em variável
                comandos.append('Utilizou write para escrever: "' + linha + '"') 


#def reconhecerRead(linha):
    #SEMPRE DAR STRIP()
    #Remover a palavra Read da frase
    #Verificar abertura de parenteses
        #Verificar se nao tem aspas simples ou duplas
            #verificar se nao começa com numero
                #verificar se fechou parenteses
                    #verificar se colocou ponto e virgula
                        #adicionar ao vetor comandos

#def reconhecerIf(linha):


#def reconhecerFor(linha):


# Função responsável por executar os comandos
# Interpretar a linha e executar o comando respectivo
# Por enquanto esse método só vai verificar que comando foi encontrado ou se aconteceu erro;
def executar():
    for item in comandos:
        print(item)



#Fluxo principal de código
comandos = []
#variaveis = []

#nomeArquivo = input('Nome do arquivo: ')

nomeArquivo = 'testeWrite.txt'

arquivo = open(nomeArquivo)

#print(arquivo)

with arquivo as info:
    for line in info.readlines():

        # A primeira palavra de cada frase é enviada em lowercase para o reconhecedor
        # De acordo com o retorno do reconhecedor será decido qual ação tomar em seguida
        primeiraPalavra = line.split()[0].lower()
        primeiraPalavra = primeiraPalavra.split('(')[0]
        primeiraPalavra = primeiraPalavra.split('=')[0]

        retorno = reconhecer(primeiraPalavra)

        if retorno == 1:
            reconhecerVar(line)
        elif retorno == 2:
            reconhecerWrite(line)

executar()
