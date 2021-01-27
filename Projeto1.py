#FP Projeto 1 - 87683 Mariana Saraiva
import math

def gera_chave1 (letras):
    '''
    Funcao que gera um tuplo de 5 tuplos com 5 elementos cada,
    que corresponde a chave utilizada nas funcoes seguintes(1)
    '''
    return (letras[0:5],letras[5:10],letras[10:15],letras[15:20],letras[20:26])
def obtem_codigo1 (car, chave):
    '''
    Funcao que obtem o codigo de um determinado caracter de acordo 
    com a linha e a coluna em que se encontra;
    o codigo consiste nos indices da linha e coluna correspondentes,
    que dependem da ordem da chave
    
    '''
    for i in range (len (chave)): # i corresponde as linhas
        for j in range(len(chave[i])): # j corresponde as colunas
            if car == chave [i][j]: 
                return str(i)+str(j)
def codifica1 (cad,chave):
    '''
    Funcao que a partir de uma cadeia de caracteres devolve
    a sequencia de algarismos correspondente, em que
    cada dois algarismos corresponde um caracter da cadeia recebida
    '''
    cad_codificada=''
    for i in range(len(cad)):
        cad_codificada = cad_codificada + obtem_codigo1(cad[i],chave)
    return cad_codificada
def obtem_car1(cod,chave):
    '''
    Funcao que, a partir dos dois digitos do codigo recebido,
    devolve o caracter correspondente tendo em conta a chave;
    os digitos do codigo sao os indices da linha e coluna
    em que o caracter se encontra na chave
    '''
    for i in range(len(chave)): # i - linhas
        for k in range (len(chave)): # k - colunas
            if cod == str(i)+str(k):
                return chave[i][k]
def descodifica1(cad_codificada,chave):
    '''
    Funcao que descodifica o codigo encriptado recebido e
    devolve a mensagem em forma de cadeia de caracteres 
    '''
    cad_descod=''
    for i in range(0,len(cad_codificada),2): # e3 = 2 porque cada letra e encriptada por dois digitos
            cad_descod=cad_descod + str (obtem_car1(cad_codificada[i:i+2],chave))
    return cad_descod
def gera_chave2(letras):
    '''
    Funcao que gera uma chave (tuplo de tuplos) em que o numero de tuplos
    depende do numero de caracteres e o ultimo tuplo pode ter menos elementos
    A chave gerada e utilizada nas funcoes seguintes (2)
    '''
    x=1
    while not (x**2 >= len(letras)): # x - numero de tuplos
        x=x+1    
    chave=()
    elementos_por_tuplo = math.ceil(len(letras)/x) # encontra o comprimento de cada tuplo
    for i in range (0,len(letras), elementos_por_tuplo): 
        chave=chave+(letras[i:i+ elementos_por_tuplo],)
    return chave

def obtem_codigo2(car, chave):
    '''
    Funcao que obtem o codigo ('linha' + 'coluna') correspondente ao caracter
    recebido tendo em conta a chave gerada anteriormente;
    se o caracter nao se encontrar na chave, retorna 'XX'
    '''
    for i in range(len(chave)): # i - linhas
    	if car in chave[i]: 
            return obtem_codigo1(car,chave)                 
    return 'XX'
def codifica2(cad,chave):
    '''
    Funcao que codifica uma cadeia de caracteres e devolve a chave de
    algarismos correspondente;
    cada caracter e codificado por dois algarismos
    Esta funcao utiliza a função obtem_codigo2, logo caso um caracter 
    nao se encontre na chave, e codificado como 'XX'
    '''
    cad_codificada2=''
    for i in range(len(cad)):
        cad_codificada2=cad_codificada2+obtem_codigo2(cad[i],chave)
    return cad_codificada2
def obtem_car2(cod,chave):
    '''
    Funcao que, ao receber um codigo de dois digitos ('linha' + 'coluna'),
    obtem o caracter que se encontra nessa posicao da chave
    Se o codigo for 'XX', (se não houver caracter correspondente) retorna '?'
    '''
    if cod == 'XX':
        return '?'
    else:
        return obtem_car1(cod,chave)
def descodifica2(cad_codificada,chave):
    '''
    Funcao que le os algarismos da cadeia recebida e descodifica
    cada par de algarismos para um caracter
    Como usa a funcao obtem_car2, se não houver a posição ('linha' + 'coluna')
    na chave, e devolvido um '?'
    '''
    cad_descod2=''
    for i in range (0,len(cad_codificada),2):
        cad_descod2=cad_descod2+str(obtem_car2(cad_codificada[i:i+2],chave))
    return cad_descod2