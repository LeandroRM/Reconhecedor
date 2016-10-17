import sys

numeroLinha = 1

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

def getNumberOfLine():
    global numeroLinha
    return str(numeroLinha)

def errorMsg(msg):
    sys.exit(msg+" na linha: "+getNumberOfLine()) 

def validateString(string):
    if (string[0] == "'" or string[0] == '"'):            
        #Verifica o fechamento da aspa
        if(string[len(string) -1] == string[0]):    
            string = string.replace(string[0], '', 2)
            string = string.strip()                                    
        else:        
            errorMsg("Erro: esperado ( "+string[0]+" ) para fechar a string")

    return string
    
def getVariavelType(var):

    tipoVariavel = False

    #Verifica se é string
    if (var[0] == "'" or var[0] == '"'):                                            
        validateString(var) #Valida a String
        tipoVariavel = "STRING"

    #Numeros 
    elif var[0].isdigit():
                    
        #Float
        if float(var):
            tipoVariavel = "FLOAT"                               
        #Inteiro
        elif int(var):
            tipoVariavel = "INTEGER"
    #Boolean
    elif (var == 'true' or var == 'false'):
        tipoVariavel = "BOOLEAN"        

    else:
        errorMsg("Erro: inesperado ( "+var[0]+" )")

    return tipoVariavel

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
        
        #Remove o ponto e virgula 
        linha = linha.replace(';', '', 1)
        linha = linha.strip()    
    
        if isVariavelValid(nomeVar):            
            linha = linha.replace(nomeVar, '', 1)
            linha = linha.strip()              

            valorVariavel = None
            tipoVariavel = None

            if(linha[0] == "="):
                linha = linha.replace("=", '', 1)
                linha = linha.strip()

                tipoVariavel = getVariavelType(linha)
            
                #Se for string vai remover as aspas
                if(tipoVariavel == 'STRING'):
                    valorVariavel = linha.replace(linha[0], '', 2).strip()
                else:
                    valorVariavel = linha                    
            
            if valorVariavel is not None:
                comandos.append('Declarou a variavel: ' + nomeVar + ' com o tipo: ' + tipoVariavel +  ' valendo: ' + valorVariavel)
            else:
                comandos.append('Declarou a variavel: ' + nomeVar)    

        else:
            errorMsg("Erro: Nome de variável invalido: "+nomeVar)
    else:
        errorMsg("Experado ';' no final ")
                                                 

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
        
        numeroLinha = numeroLinha+1

executar()
