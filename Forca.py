import random
plv = ['abacaxi', 'ortodoxo', 'corno', 'boi', 'celular', 'burro', 'vaca', 'bola', 'relativo', 'mae', 'coito', 'pipa', 'pao', 'utopia', 'sexo', 'alduterio', 'fofa', 'tigre', 'legado', 'roxo', 'prato', 'democracia', 'nostalgia', 'divergente', 'lealdade', 'relevancia']
alf = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
vic = False
df = False
tv = False
dfp = 0
n = random.choice(plv)
nt = len(n)

if n[0] in alf:
    a = n[0]
if n[1] in alf:
    b = n[1]
if n[2] in alf:
    c = n[2]
try:
    if n[3] in alf:
        d = n[3]
except:
    d = (' ')
try:
    if n[4] in alf:
        e = n[4]
except:
    e = (' ')
try:
    if n[5] in alf:
        f = n[5]
except:
    f = (' ')
try:
    if n[6] in alf:
        g = n[6]
except:
    g = (' ')
try:
    if n[7] in alf:
        h = n[7]
except:
    h = (' ')
try:
    if n[8] in alf:
        i = n[8]
except:
    i = (' ')
try:
    if n[9] in alf:
        j = n[9]
except:
    j = (' ')
if n[0] in alf:
    Aa = '_'
if n[1] in alf:
    Bb = '_'
if n[2] in alf:
    Cc = '_'
try:
    if n[3] in alf:
        Dd = '_'
except:
    Dd = (' ')
try:
    if n[4] in alf:
        Ee = '_'
except:
    Ee = (' ')
try:
    if n[5] in alf:
        Ff = '_'
except:
    Ff = (' ')
try:
    if n[6] in alf:
        Gg = '_'
except:
    Gg = (' ')
try:
    if n[7] in alf:
        Hh = '_'
except:
    Hh = (' ')
try:
    if n[8] in alf:
        Ii = '_'
except:
    Ii = (' ')
try:
    if n[9] in alf:
        Jj = '_'
except:
    Jj = (' ')
print('Bem-vindo ao jogo da Forca\n')
print('Uma palavra com 10 letras ou menos será selecionada\n')
print('Você terá um máximo de 6 chances para acertar\n')
for nb in range(nt):
    print('_', end = ' ')
print('\n')
print('A palavra tem ' + str(nt) + ' letras\n')
while vic == False and df == False:
    while tv == False:
        print('\n')
        es = input('Escolha uma letra: \n')
        if es in alf:
            tv = True
    tv = False
    if es == a:
        Aa = a
    if es == b:
        Bb = b
    if es == c:
        Cc = c
    if es == d:
        Dd = d
    if es == e:
        Ee = e
    if es == f:
        Ff = f
    if es == g:
        Gg = g
    if es == h:
        Hh = h
    if es == i:
        Ii = i
    if es == j:
        Jj = j
    if es not in n:
        dfp = dfp + 1
    print(Aa, Bb, Cc, Dd, Ee, Ff, Gg, Hh, Ii, Jj)
    print('\n')
    if dfp >= 1:
        print('  O  ')
    if dfp == 2:
        print('  |  ')
    if dfp == 3:
        print(' /|  ')
    if dfp >= 4:
        print(' /|\ ')
    if dfp == 5:
        print(' /   ')
    if dfp == 6:
        print(' / \ ')   
    if (Aa == a) and (Bb == b) and (Cc == c) and (Dd == d) and (Ee == e) and (Ff == f) and (Gg == g) and (Hh == h) and (Ii == i) and ( Jj == j):
        vic = True
    if dfp == 6:
        df = True
print('\n')
if vic == True:
    print('VITÓRIA')
if df == True:
    print('FORCA')
input()