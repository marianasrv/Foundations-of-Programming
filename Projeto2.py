# Projeto 2 - 87683 Mariana Saraiva

def faz_pos(l,c):
    '''
    Funcao que devolve um tuplo de dois numeros inteiros nao negativos
    (apenas sao aceites argumentos deste tipo);
    l corresponde a linha e c a coluna; (l,c) e o tuplo do tipo posicao
    '''
    if not (isinstance (l,int)) or l < 0:
        raise ValueError ('faz_pos: argumentos errados')
    if not (isinstance (c,int)) or c < 0:
        raise ValueError ('faz_pos: argumentos errados')
    else:
        return (l,c)
    
def linha_pos(p):
    '''
    Recebe p do tipo posicao e devolve a linha correspondente
    '''
    return p[0]

def coluna_pos(p):
    '''
    Recebe p do tipo posicao e devolve a coluna correspondente
    '''
    return p[1]

def e_pos (arg):
    '''
    Funcao que verifica se o argumento que recebe e do tipo posicao
    e devolve True caso se verifique e False caso contrario
    '''
    return isinstance (arg, tuple) and len(arg) == 2 and \
           isinstance(linha_pos(arg), int) and linha_pos(arg) >= 0 and \
           isinstance(coluna_pos(arg), int) and coluna_pos(arg) >= 0

def pos_iguais(p1,p2):
    '''
    A funcao pos_iguais compara dois argumentos do tipo posicao e
    retorna True se forem iguais e False caso contrario
    '''
    return e_pos(p1) and e_pos(p2) and p1 == p2
    
def gera_chave_aux(l, mgc):
    '''
    Funcao auxiliar para gerar uma chave com tamanho = 25 e com as
    caractericas pedidas: 
    comeca-se por colocar as letras da mensagem (mgc) e se aparecerem mais do
    que uma vez, so sera inserida na chave a sua primeira ocorrencia; o resto
    da chave e completado pelas letras de l que ainda nao estao na chave
    '''
    chave = []
        
    for car in mgc:
        if not car in chave:

            if not car == ' ':
                chave += [car]
                
    for car in l:
        if car not in chave: 
            chave +=[car]
                
    return chave

def gera_chave_linhas(l,mgc):
    '''
    Esta funcao utiliza a funcao gera_chave_aux de modo a gerar a chave como
    uma tabela de 5x5 isto e, divide a chave gerada na funcao auxiliar em
    listas de 5 elementos formando uma lista de 5 listas
    '''
    L = tuple('ABCDEFGHIKLMNOPQRSTUVWXYZ')
    
    if len(l) != 25:
        raise ValueError ('gera_chave_linhas: argumentos errados')
    
    for i in range(len(l)):
        if l[i] in l[0:i]:
            raise ValueError ('gera_chave_linhas: argumentos errados')
        
    for letra in mgc:
        if not letra in L:
            if not letra == ' ':
                raise ValueError ('gera_chave_linhas: argumentos errados')
    
    chave1 = []
    chave = gera_chave_aux(l, mgc)
    inicio = 0
    final = 5
            
    while final <= len(chave):
        chave1 += [chave[inicio:final]]
        inicio += 5
        final += 5
           
    return chave1

def gera_chave_espiral(l, mgc, s, pos):
    '''
    Funcao que gera uma mensagem escrita numa tabela 5x5 em forma de espiral
    O sentido e a posicao inicial podem variar; sao utilizadas algumas funcoes
    auxiliares (muda_chave e posicoes_espiral)
    '''
    L = tuple('ABCDEFGHIKLMNOPQRSTUVWXYZ')
    
    if len(l) != 25:
        raise ValueError ('gera_chave_espiral: argumentos errados')
    
    for i in range(len(l)): # cada letra so pode aparacer uma vez
        if l[i] in l[0:i]:
            raise ValueError ('gera_chave_espiral: argumentos errados')
        
    for letra in mgc:
        if not letra == ' ':
            if not letra in L: # nao sao aceites outros caracteres alem dos de L
                raise ValueError ('gera_chave_espiral: argumentos errados')
    
    if s != 'r' and s!= 'c':
        raise ValueError ('gera_chave_espiral: argumentos errados')
    
    if not (isinstance(pos, tuple)):
        raise ValueError ('gera_chave_espiral: argumentos errados')
    
    chave = gera_chave_aux(l, mgc)
    chave1 = gera_chave_linhas(l, mgc)    
        
    for i in range(len(chave)):
        chave2 = muda_chave(chave1, posicoes_espiral(s,pos)[i],chave[i])
               
    return chave2
    
def posicoes_espiral(s, pos):
    '''
    Funcao auxiliar da funcao gera_chave_espiral; Esta funcao recebe o
    sentido e posicao onde vai comecar a ser escrita a mensagem
    
    De acordo com os parametros recebidos, recorre a uma outra funcao 
    auxiliar (posicoes_aux) de modo a indicar o sentido inicial
    '''
    c_inf = 0 # primeiro indice da coluna
    c = 4  # indice maximo da coluna
    li = 4 # primeiro indice da linha
    l_inf = 0 # indice maximo da linha
    p = ()

    while c != c_inf and li != l_inf:
                  
        if s == 'r' and pos == faz_pos(l_inf,c_inf) or s == 'c' and \
           pos == faz_pos(li,c_inf):
            return posicoes_aux(s, 0,1, pos)
                  
        if s == 'r' and pos == faz_pos(l_inf,c) or s == 'c' and \
           pos == faz_pos(l_inf,c_inf):
            return posicoes_aux(s,1, 0, pos)
                  
        if s == 'r' and pos == faz_pos(li,c) or  s== 'c' and \
           pos == faz_pos(l_inf,c):
            return posicoes_aux(s,0,-1, pos)
                  
        if s == 'r' and pos == faz_pos(li,c_inf) or s == 'c' and \
           pos == faz_pos(li,c):
            return  posicoes_aux(s, -1, 0, pos) 
      
        return p    
        
def posicoes_aux(s, s1, s2, pos):
    '''
    Funcao auxiliar que recebe o sentido(s : 'r' ou 'c'), a orientacao
    (s1 - linha; s2 - coluna) em que comeca de acordo com s e a posicao inicial
    Retorna um tuplo de tuplos com as posicoes (l,c) que as letras da mensagem
    irao ocupar (por ordem) de forma a formar uma espiral
    Utiliza uma outra funcao auxiliar (mudar_sentido)
    '''
    m_inf = 0 # menor valor (indice) que a linha pode tomar
    n_inf = 0 # menor valor (indice) que a coluna pode tomar
    m = 5 # numero de linhas 
    n = 5 # numero de colunas
    p = () 
    p1 = () 
            
    while  n_inf <= n:
                
        if s == 'c':
                
            if (s1,s2) == (0, 1):  # desloca-se para a direita na mesma linha
                for i in range (n_inf,n):
                    p +=(m - 1, i,)
                    
                m -= 1
                (s1, s2) = mudar_sentido(s, s1, s2)
                    
            if (s1,s2) == (1, 0): # desloca-se para baixo, na mesma coluna
                for i in range (m_inf, m):
                    p +=  (i,n_inf,)
                    
                n_inf +=1
                (s1, s2) = mudar_sentido(s, s1, s2)
                    
            if (s1,s2) == (0, -1): # desloca-se para a esquerda numa linha
                for i in range(n - 1, n_inf - 1 , -1):
                    p += (m_inf,i,)
                        
                m_inf += 1
                (s1, s2) = mudar_sentido(s, s1, s2)
                    
            if (s1,s2) == (-1, 0): # anda para cima, numa coluna
                for i in range (m - 1, m_inf - 1, -1):
                    p += (i, n - 1,)
                    
                n -= 1
                (s1, s2) = mudar_sentido(s, s1, s2)
                
        if s == 'r':
                    
            if (s1,s2) == (0, 1):
                for i in range (n_inf,n):
                    p += (m_inf,i,)
                                
                m_inf += 1
                (s1, s2) = mudar_sentido(s, s1, s2)
                                
            if (s1,s2) == (1, 0):
                for i in range (m_inf, m):
                    p +=  (i,n-1,)
                                
                n -=1
                (s1, s2) = mudar_sentido(s, s1, s2)
                                
            if (s1,s2) == (0, -1):
                for i in range(n - 1, n_inf - 1 , -1):
                    p += (m-1,i,)
                                    
                m -= 1
                (s1, s2) = mudar_sentido(s, s1, s2)
                                
            if (s1,s2) == (-1, 0):
                for i in range (m - 1, m_inf - 1, -1):
                    p += (i,n_inf,)
                                
                n_inf += 1
                (s1, s2) = mudar_sentido(s, s1, s2)            
            
    inicio = 0
    final = 2
                                    
    while final <= len(p):
        p1 += (p[inicio:final],)
        inicio += 2
        final += 2
                
    return p1
        
def mudar_sentido(s, s1, s2):
    '''
    Funcao auxiliar que, de acordo com o sentido em que esta a percorrer
    a matriz (s) e com a orientacao que acaba de percorrer, devolve a 
    direcao seguinte de modo a fazer uma espiral
    '''
    if s == 'r' and s1 == -1 and s2 == 0 or \
       s == 'c' and s1 == 1 and s2 == 0:
        (s1, s2) = (0, 1)
        
    elif s == 'r' and s1 == 0 and s2 == 1 or \
         s == 'c' and s1 == 0 and s2 == -1:
        (s1, s2) = (1, 0)
            
    elif s == 'r' and s1 == 1 and s2 == 0 or \
         s == 'c' and s1 == -1 and s2 == 0:
        (s1, s2) = (0, -1)
        
    elif s == 'r' and s1 == 0 and s2 == -1 or \
         s == 'c' and s1 == 0 and s2 == 1:
        (s1, s2) = (-1, 0) 
            
    return (s1, s2)
    
def ref_chave(c,p):
    '''
    Funcao que recebe uma chave(c) e uma posicao(p) e devolve o caracter
    que esta na posicao p da chave c
    '''
    return c[p[0]][p[1]]

def muda_chave (c, p, l):
    '''
    A funcao muda_chave altera a chave (c) na posicao(p), isto e, substitui
    a letra que esta na posicao p nessa chave pelo caracter dado (l)
    '''
    c [p[0]][p[1]] = l
    return c

def e_chave(arg):
    '''
    Funcao que verifica se o argumento recebido e do tipo chave(tabela 5x5)
    '''
    l = ['A','B','C','D','E','F','G','H','I','K','L','M','N',\
         'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    if len(arg) != 5:
        return False
    
    for i in range (len(arg)):
        if len(arg[i]) != 5:
            return False
        else:    
            for j in range(len(arg[i])):
                if not arg[i][j] in l:
                    return False
    else:
        return True
       
def string_chave(c):
    '''
    Funcao que devolve uma cadeia de caracteres que ao ser impressa apresenta
    as letras da chave(c) dispostas numa tabela 5x5
    '''
    str_chave = ''
    for i in range(len(c)):
        for j in range(len(c[i])):
            if j == 4:
                str_chave += c[i][j] + ' \n'
            else:
                str_chave += c[i][j] + ' '
            
    return str_chave

def digramas(mens):
    '''
    Funcao que recebe uma cadeia de caracteres (mens) e devolve a cadeia de
    caracteres correspondente aos digramas (sequencia de 2 letras consecutivas)
    transformados; se o digrama tiver as duas letras iguais,insere-se um 'X' na
    segunda posicao e a mensagem desloca-se uma posicao para a direita
    '''
    mens_transf = ''
    
    for i in range(len(mens)):
        if not mens[i] == ' ': # retiram-se os espacos
            mens_transf += mens[i]
            
    i = 1
    while i < len(mens_transf):
        
        if mens_transf[i] == mens_transf[i-1]:
            mens_transf= mens_transf[0:i] + 'X' + mens_transf[i:]   
        i +=2
            
    if len(mens_transf) % 2 != 0: # se no final, o tamanho for numero
        mens_transf +='X' # impar, adiciona-se um 'X' ao ultimo digrama
        
    return mens_transf
   
def figura (digrm, chave):
    '''
    A funcao figura recebe um digrama e uma chave e devolve um tuplo de 3
    elementos (1: figura determinada pelas letras do digrama ('l', 'c' ou 'r')
    2 e 3: posicoes ocupadas pela primeira e segunda letras do digrama na chave,
    respetivamente)
    '''
    digrm = list (digrm)
    
    numCoord = 0
    i = 0
    while i < len(chave) and numCoord < 2:
        j = 0
        while j < len(chave) and numCoord < 2:
            if chave[i][j] == digrm[0]:
                pos1 = faz_pos(i,j)
                numCoord += 1
            else:
                if chave[i][j] == digrm[1]:
                    pos2 = faz_pos(i,j)
                    numCoord +=1
            j += 1
        i += 1

    if pos1[0] == pos2[0]: # se estao na mesma linha: fig = 'l'
        fig = 'l'
    elif pos1[1] == pos2[1]: # se estao na mesma coluna: fig = 'c'
        fig = 'c'
    else: # se estao em linhas e colunas diferentes: fig = 'r'
        fig = 'r'
    
    return (fig, pos1, pos2)

def codifica_l(pos1, pos2, inc):
    '''
    Funcao que recebe as posicoes das letras de um digrama na mesma linha
    de uma chave (pos1 e pos2) e inc, que poderá ser 1 (encriptacao) ou -1
    (desencriptacao).
    Devolve um tuplo (pos1_cod, pos2_cod) com as posicoes das letras do digrama
    encriptado/desencriptado; recorre a uma funcao auxiliar (cod_l_aux)
    '''
    
    def cod_l_aux(pos, inc):
        '''
        Funcao auxiliar que, permite encontrar pos1_cod e pos2_cod.
        Quando inc = 1, "anda para a direita" uma unidade na coluna;
        quando inc = -1, desloca-se para a esquerda.
        '''
        if inc == 1:
            if coluna_pos(pos) == 4: # se estiver na coluna 4, passa para a coluna 0
                pos_cod = (linha_pos(pos), 0)
            else:
                pos_cod = (linha_pos(pos), coluna_pos(pos) + 1)
            return pos_cod
        if inc == -1:
            if coluna_pos(pos) == 0: # se estiver na coluna 0, passa para a coluna 4
                pos_cod = (linha_pos(pos), 4)
            else:
                pos_cod = (linha_pos(pos), coluna_pos(pos) -1)
            return pos_cod
    
    if inc == 1:
        pos1_cod = cod_l_aux(pos1, 1)
        pos2_cod = cod_l_aux (pos2, 1)
        
    if inc == -1:
        pos1_cod = cod_l_aux (pos1, -1)
        pos2_cod = cod_l_aux(pos2, -1)
    
    return (pos1_cod, pos2_cod)

def codifica_c(pos1, pos2, inc):
    '''
    Funcao que recebe as posicoes das letras de um digrama na mesma coluna
    de uma chave (pos1 e pos2) e inc, que poderá ser 1 (encriptacao) ou -1
    (desencriptacao).
    A função devolve um tuplo (pos1_cod, pos2_cod) com as posicoes das letras
    do digrama encriptado/desencriptado.
    '''
    
    def cod_c_aux(pos, inc):
        '''
        Funcao auxiliar para facilitar determinar pos1_cod e pos2_cod
        Quando inc = 1, a linha aumenta; quando inc = -1, a linha diminui
        '''
        if inc == 1:
            if linha_pos(pos) == 4: # se estiver na linha 4, passa para a linha 0
                pos_cod = (0, coluna_pos(pos))
            else:
                pos_cod = (linha_pos(pos) + 1, coluna_pos(pos))
            return pos_cod
        if inc == -1:
            if linha_pos(pos) == 0: # se estiver na linha 0, passa para a linha 4
                pos_cod = (4, coluna_pos(pos))
            else:
                pos_cod = (linha_pos(pos) - 1, coluna_pos(pos))
            return pos_cod
        
    if inc == 1:
        pos1_cod = cod_c_aux(pos1, 1)
        pos2_cod = cod_c_aux (pos2, 1)
        
    if inc == -1:
        pos1_cod = cod_c_aux (pos1, -1)
        pos2_cod = cod_c_aux(pos2, -1)
        
    return (pos1_cod, pos2_cod)

def codifica_r(pos1, pos2):
    '''
    Funcao que recebe duas posicoes que se encontram em linhas e colunas
    diferentes
    pos1_cod fica com a mesma linha que pos1 e com a coluna de pos2; pos2_cod
    fica com a mesma linha que pos2 e com a coluna de pos1
    '''
    pos1_cod = faz_pos(pos1[0], pos2[1])
    pos2_cod = faz_pos(pos2 [0], pos1[1])
    
    return (pos1_cod, pos2_cod)

def codifica_digrama(digrm, chave, inc):
    '''
    Esta funcao usa a funcao figura para ver a posicao das letras do digrama
    A partir dai utiliza as funcoes codifica (l, c, ou r) correspondentes tendo
    em conta as posicoes das letras do digrama
    Sao devolvidas as letras que correspondem a encriptacao(inc = 1)/
    desencriptacao(inc = -1) do digrama
    '''
    figura_0 = figura(digrm, chave)[0]
    figura_1 = figura(digrm,chave)[1]
    figura_2 = figura(digrm,chave)[2]
    
    if figura_0 == 'l':
        return ref_chave(chave, (codifica_l(figura_1, figura_2, inc)[0])) + \
               ref_chave(chave, (codifica_l(figura_1, figura_2, inc)[1]))
    
    elif figura_0 == 'c':
        return ref_chave(chave, (codifica_c(figura_1, figura_2, inc)[0])) + \
               ref_chave(chave, (codifica_c(figura_1, figura_2, inc)[1]))
    elif figura_0 == 'r':
        return ref_chave(chave, (codifica_r(figura_1, figura_2)[0])) + \
               ref_chave(chave, (codifica_r(figura_1, figura_2)[1]))
    
def codifica(mens, chave, inc):
    '''
    Funcao que recebe uma cadeia de caracteres e devolve a sua mensagem
    encriptada  (inc = 1) ou desencriptada (inc = -1); e utilizada a funcao
    codifica_digrama
    '''
    mens_codificada = ''
    mens =(digramas(mens))
    
    for i in range (0, len(mens), 2):
        mens_codificada += codifica_digrama((mens[i:i+2]), chave, inc)
        
    return mens_codificada