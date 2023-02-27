a = '_'
b = '_'
c = '_'
d = '_'
e = '_'
f = '_'
g = ' '
h = ' '
i = ' '
vica = False
vicb = False
draw = False
validA = False
validB = False
A1 = False
A2 = False
A3 = False
A4 = False
A5 = False
A6 = False
A7 = False
A8 = False
A9 = False
B1 = False
B2 = False
B3 = False
B4 = False
B5 = False
B6 = False
B7 = False
B8 = False
B9 = False

print('Bem-vindo ao Jogo da Velha\n')
print('Dois jogadores são necessários')
print('Jogador A joga primeiro e é o círculo')
print('Jogador B joga depois e é o xis\n')
print('Para jogar escolha em sua vez um número de 1 a 9')
print('Essas são as posições:\n')
print('_1_|_2_|_3_')
print('_4_|_5_|_6_')
print(' 7 | 8 | 9 \n')
while vica == False and vicb == False and draw == False:
    while validA == False:    
        while True:
            try:
                print('Escolha de 1 a 9 para decidir onde marcar\n')
                jogA = int(input('Jogador A: '))
                break
            except:
                print('\n')
                print('Jogada Inválida\n')
        print('\n')  
        if jogA == 1 and B1 == False:
            A1 = True
            a = 'o'
            validA = True      
        elif jogA == 2 and B2 == False:
            A2 = True
            b = 'o'
            validA = True 
        elif jogA == 3 and B3 == False:       
            A3 = True
            c = 'o'  
            validA = True      
        elif jogA == 4 and B4 == False:       
            A4 = True
            d = 'o'  
            validA = True      
        elif jogA == 5 and B5 == False:        
            A5 = True
            e = 'o' 
            validA = True       
        elif jogA == 6 and B6 == False:        
            A6 = True
            f = 'o'  
            validA = True      
        elif jogA == 7 and B7 == False:        
            A7 = True
            g = 'o' 
            validA = True        
        elif jogA == 8 and B8 == False:        
            A8 = True
            h = 'o' 
            validA = True        
        elif jogA == 9 and B9 == False:        
            A9 = True
            i = 'o'
            validA = True
        else:
            print('Jogada Inválida\n')      
    print('_' + a + '_|_' + b + '_|_' + c + '_')
    print('_' + d + '_|_' + e + '_|_' + f + '_')
    print(' ' + g + ' | ' + h + ' | ' + i + ' \n')
    if A1 == True and A2 == True and A3 == True:
        vica = True
        break
    elif A4 == True and A5 == True and A6 == True:
        vica = True
        break
    elif A7 == True and A8 == True and A9 == True:
        vica = True
        break
    elif A1 == True and A4 == True and A7 == True:
        vica = True
        break
    elif A2 == True and A5 == True and A8 == True:
        vica = True
        break
    elif A3 == True and A6 == True and A9 == True:
        vica = True
        break
    elif A1 == True and A5 == True and A9 == True:
        vica = True
        break
    elif A3 == True and A5 == True and A7 == True:
        vica = True
        break
    elif (A1 == True or B1 == True) and (A2 == True or B2 == True) and (A3 == True or B3 == True) and (A4 == True or B4 == True) and (A5 == True or B5 == True) and (A6 == True or B6 == True) and (A7 == True or B7 == True) and (A8 == True or B8 == True) and (A9 == True or B9 == True):
        draw = True
        break
    print('\n')
    validA = False
    while validB == False:
        while True:
            try:
                print('Escolha de 1 a 9 para decidir onde marcar\n')
                jogB = int(input('Jogador B: '))
                break
            except:
                print('\n')
                print('Jogada Inválida\n')
        print('\n')  
        if jogB == 1 and A1 == False:
            B1 = True
            a = 'x' 
            validB = True
        elif jogB == 2 and A2 == False:
            B2 = True
            b = 'x'
            validB = True
        elif jogB == 3 and A3 == False:       
            B3 = True
            c = 'x'  
            validB = True     
        elif jogB == 4 and A4 == False:       
            B4 = True
            d = 'x'  
            validB = True     
        elif jogB == 5 and A5 == False:        
            B5 = True
            e = 'x'   
            validB = True    
        elif jogB == 6 and A6 == False:        
            B6 = True
            f = 'x'  
            validB = True     
        elif jogB == 7 and A7 == False:        
            B7 = True
            g = 'x'  
            validB = True      
        elif jogB == 8 and A8 == False:        
            B8 = True
            h = 'x' 
            validB = True       
        elif jogB == 9 and A9 == False:        
            B9 = True
            i = 'x'
            validB = True
        else:
            print('Jogada Inválida\n')  
    print('_' + a + '_|_' + b + '_|_' + c + '_')
    print('_' + d + '_|_' + e + '_|_' + f + '_')
    print(' ' + g + ' | ' + h + ' | ' + i + ' \n')
    if B1 == True and B2 == True and B3 == True:
        vicb = True
    elif B4 == True and B5 == True and B6 == True:
        vicb = True
    elif B7 == True and B8 == True and B9 == True:
        vicb = True
    elif B1 == True and B4 == True and B7 == True:
        vicb = True
    elif B2 == True and B5 == True and B8 == True:
        vicb = True
    elif B3 == True and B6 == True and B9 == True:
        vicb = True
    elif B1 == True and B5 == True and B9 == True:
        vicb = True
    elif B3 == True and B5 == True and B7 == True:
        vicb = True
    validB = False
if vica == True:
    print('Vencedor: Jogador A')
elif vicb == True:
    print('Vencedor: Jogador B')
elif draw == True:
    print('Empate')
input()     
        