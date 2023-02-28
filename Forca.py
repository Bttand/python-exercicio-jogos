import random
lista = ['abacaxi', 'ortodoxo', 'corno', 'boi', 'celular', 'burro', 'vaca', 'bola', 'relativo', 'mae', 'coito', 'pipa', 'pao', 'utopia', 'sexo', 'adulterio', 'fofa', 'tigre', 'legado', 'roxo', 'prato', 'democracia', 'nostalgia', 'divergente', 'lealdade', 'relevancia']
alfabeto = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Aa = ' '
Bb = ' '
Cc = ' '
Dd = ' '
Ee = ' '
Ff = ' '
Gg = ' '
Hh = ' '
Ii = ' '
Jj = ' '
erro = ["_", "_", "_", "_", "_", "_"]
x = 0
vitoria = False
derrota = False
teste = False
tentativas = 0
palavra = random.choice(lista)
plvalor = len(palavra)

a = palavra[0]
b = palavra[1]
c = palavra[2]
try:
    if palavra[3] in alfabeto:
        d = palavra[3]
except:
    d = (' ')
try:
    if palavra[4] in alfabeto:
        e = palavra[4]
except:
    e = (' ')
try:
    if palavra[5] in alfabeto:
        f = palavra[5]
except:
    f = (' ')
try:
    if palavra[6] in alfabeto:
        g = palavra[6]
except:
    g = (' ')
try:
    if palavra[7] in alfabeto:
        h = palavra[7]
except:
    h = (' ')
try:
    if palavra[8] in alfabeto:
        i = palavra[8]
except:
    i = (' ')
try:
    if palavra[9] in alfabeto:
        j = palavra[9]
except:
    j = (' ')
Aa = '_'
Bb = '_'
Cc = '_'
try:
    if palavra[3] in alfabeto:
        Dd = '_'
except:
    Dd = (' ')
try:
    if palavra[4] in alfabeto:
        Ee = '_'
except:
    Ee = (' ')
try:
    if palavra[5] in alfabeto:
        Ff = '_'
except:
    Ff = (' ')
try:
    if palavra[6] in alfabeto:
        Gg = '_'
except:
    Gg = (' ')
try:
    if palavra[7] in alfabeto:
        Hh = '_'
except:
    Hh = (' ')
try:
    if palavra[8] in alfabeto:
        Ii = '_'
except:
    Ii = (' ')
try:
    if palavra[9] in alfabeto:
        Jj = '_'
except:
    Jj = (' ')
print('Bem-vindo ao jogo da Forca\n')
print('Uma palavra com 10 letras ou menos será selecionada\n')
print('Você terá um máximo de 6 chances para acertar\n')
for nb in range(plvalor):
    print('_', end = ' ')
print('\n')
print('A palavra tem ' + str(plvalor) + ' letras')
while vitoria == False and derrota == False:
    while teste == False:
        print('\n')
        letra = input('Escolha uma letra' + ' [tentativas: ' + erro[0] + " " + erro[1] + " " + erro[2] + " " + erro[3] + " " + erro[4]+ " " + erro[5] + " ]\n")
        if letra in alfabeto:
            if letra not in erro:
                teste = True
    teste = False
    if letra == a:
        Aa = a
    if letra == b:
        Bb = b
    if letra == c:
        Cc = c
    if letra == d:
        Dd = d
    if letra == e:
        Ee = e
    if letra == f:
        Ff = f
    if letra == g:
        Gg = g
    if letra == h:
        Hh = h
    if letra == i:
        Ii = i
    if letra == j:
        Jj = j
    if letra not in palavra:
        tentativas = tentativas + 1
        erro[x] = letra
        x = x + 1
    print(Aa, Bb, Cc, Dd, Ee, Ff, Gg, Hh, Ii, Jj)
    print('\n')
    if tentativas >= 1:
        print('  O  ')
    if tentativas == 2:
        print('  |  ')
    if tentativas == 3:
        print(' /|  ')
    if tentativas >= 4:
        print(' /|\ ')
    if tentativas == 5:
        print(' /   ')
    if tentativas == 6:
        print(' / \ ')   
    if (Aa == a) and (Bb == b) and (Cc == c) and (Dd == d) and (Ee == e) and (Ff == f) and (Gg == g) and (Hh == h) and (Ii == i) and ( Jj == j):
        vitoria = True
    if tentativas == 6:
        derrota = True
print('\n')
if vitoria == True:
    print('VITÓRIA')
if derrota == True:
    print('FORCA')
    print('\nErros: ', erro)
    print('Palavra: ', palavra)
input()