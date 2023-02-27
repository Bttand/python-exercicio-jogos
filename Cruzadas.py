import random
a = [' p', 'a', 'v', 'j', 'a', 'g', 'a', 'g', '\n', 'w', 'b', 'a', 't', 'e', 'r', 's', 'o', '\n', 'z', 'o', 'b', 's', 'g', 'p', 'k', 'r', '\n', 'x', 'l', 'c', 'c', 'a', 'z', 'a', 'r', '\n', 's', 'a', 'o', 'o', 'h', 'v', 'o', 'q', '\n', 's', 't', 'y', 'i', 'u', 'k', 'i', 't', '\n', 'v', 'p', 'j', 's', 'c', 'j', 's', 'u', '\n', 'p', 'e', 'n', 'a', 'g', 'o', 'a', 'o', '\n']
b = [' w', 't', 'b', 'w', 'j', 'v', 'c', 'o', '\n', 'j', 'b', 's', 'g', 'p', 'k', 'a', 's', '\n', 'z', 'r', 'n', 'v', 'g', 'o', 'f', 'o', '\n', 'p', 'p', 'v', 'j', 'a', 'g', 'e', 'g', '\n', 'v', 'o', 'j', 'm', 'c', 'j', 'y', 'u', '\n', 'g', 'u', 'c', 'a', 'r', 'a', 'r', 'a', '\n', 'f', 'c', 'e', 'l', 'u', 'l', 'a', 'r', '\n', 'x', 'o', 'g', 'b', 't', 'h', 't', 'z', '\n']
c = [' m', 'a', 't', 'o', 't', 'h', 't', 'z', '\n', 'o', 'a', 'g', 'b', 't', 'h', 't', 'z', '\n', 'r', 'v', 'u', 'u', 'c', 'u', 'b', 'o', '\n', 'a', 'p', 'j', 'e', 's', 'r', 'q', 't', '\n', 'd', 'p', 'b', 'l', 'e', 'u', 'j', 'y', '\n', 'i', 'h', 'u', 'd', 'd', 'b', 'r', 'e', '\n', 'a', 'c', 'a', 'i', 'r', 'u', 't', 'u', '\n', 'a', 's', 'e', 'n', 't', 'a', 'r', 'x', '\n']
i = 0
A1 = False
A2 = False
A3 = False
A4 = False
A5 = False
B1 = False
B2 = False
B3 = False
B4 = False
C1 = False
C2 = False
C3 = False
C4 = False
C5 = False
C6 = False
vitoria = False
lista = [a, b, c]
escolha = random.choice(lista)

print('Bem-vindo ao Caça Palavras\n\nUm quadro com letras aleatórias foi escolhido para você com um número x de palavras escondidas\n\nBoa sorte para encontra-las\n')
for n in escolha:
    print(escolha[i], end = ' ')
    i = i + 1
if escolha == a:
    quanplv = 5
if escolha == b:
    quanplv = 4
if escolha == c:
    quanplv = 6
print('\n')
print('Existem ' + str(quanplv) + ' palavras\n')
while vitoria == False:
    if escolha == a:
        try:
            tnt = str(input('Achou alguma palavra? '))
            if tnt == ('coisa'): 
                if A1 == True:
                    print('Palavra já encontrada, tente outra\n')
                if A1 == False:
                    A1 = True
                    print('Correto\n')
            elif tnt == ('azar'): 
                if A2 == True:
                    print('Palavra já encontrada, tente outra\n')
                if A2 == False:
                    A2 = True
                    print('Correto\n')
            elif tnt == ('bola'): 
                if A3 == True:
                    print('Palavra já encontrada, tente outra\n')
                if A3 == False:
                    A3 = True
                    print('Correto\n')
            elif tnt == ('pena'): 
                if A4 == True:
                    print('Palavra já encontrada, tente outra\n')
                if A4 == False:
                    A4 = True
                    print('Correto\n')
            elif tnt == ('bater'): 
                if A5 == True:
                    print('Palavra já encontrada, tente outra\n')
                if A5 == False:
                    A5 = True
                    print('Correto\n')
            else:
                print('Errado')
        except:
            print('Errado')
    if A1 == True and A2 == True and A3 == True and A4 == True and A5 == True:
        vitoria = True
    if escolha == b:
        try:
            tnt = str(input('Achou alguma palavra? '))
            if tnt == ('arara'): 
                if B1 == True:
                    print('Palavra já encontrada, tente outra\n')
                if B1 == False:
                    B1 = True
                    print('Correto\n')
            elif tnt == ('cafe'): 
                if B2 == True:
                    print('Palavra já encontrada, tente outra\n')
                if B2 == False:
                    B2 = True
                    print('Correto\n')
            elif tnt == ('pouco'): 
                if B3 == True:
                    print('Palavra já encontrada, tente outra\n')
                if B3 == False:
                    B3 = True
                    print('Correto\n')
            elif tnt == ('celular'): 
                if B4 == True:
                    print('Palavra já encontrada, tente outra\n')
                if B4 == False:
                    B4 = True
                    print('Correto\n')
            else:
                print('Errado')
        except:
            print('Errado')
    if B1 == True and B2 == True and B3 == True and B4 == True:
        vitoria = True
    if escolha == c:
        try:
            tnt = str(input('Achou alguma palavra? '))
            if tnt == ('moradia'): 
                if C1 == True:
                    print('Palavra já encontrada, tente outra\n')
                if C1 == False:
                    C1 = True
                    print('Correto\n')
            elif tnt == ('mato'): 
                if C2 == True:
                    print('Palavra já encontrada, tente outra\n')
                if C2 == False:
                    C2 = True
                    print('Correto\n')
            elif tnt == ('cubo'): 
                if C3 == True:
                    print('Palavra já encontrada, tente outra\n')
                if C3 == False:
                    C3 = True
                    print('Correto\n')
            elif tnt == ('sentar'): 
                if C4 == True:
                    print('Palavra já encontrada, tente outra\n')
                if C4 == False:
                    C4 = True
                    print('Correto\n')
            elif tnt == ('urubu'): 
                if C5 == True:
                    print('Palavra já encontrada, tente outra\n')
                if C5 == False:
                    C5 = True
                    print('Correto\n')
            elif tnt == ('cair'): 
                if C6 == True:
                    print('Palavra já encontrada, tente outra\n')
                if C6 == False:
                    C6 = True
                    print('Correto\n')
            else:
                print('Errado')
        except:
            print('Errado')
    if C1 == True and C2 == True and C3 == True and C4 == True and C5 == True and C3 == True:
        vitoria = True          
if vitoria == True:
    print('VITÓRIA')
input()