##Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido
# quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no
#final do jogo

import math
import random
print('Jogo : Par ou Ímpar ?')
print('-' * 25)
ab = 0
cont= 0
soma = 0

while ab != 5:
    num = int(input('Digite um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I] ? ')).strip().upper()
    comp = random.randint(1,11)
    soma = num + comp
    print(f'Você jogou {num} e o computador {comp}.')

    if opcao == 'P':
        if soma % 2 == 0:
            print('Sua opção PAR')
            print(f'A soma é {soma}.É PAR. VOCÊ GANHOU!!')
            cont = cont + 1
        else:
            print('Sua opção PAR')
            print(f'A soma é {soma}.É IMPAR. VOCÊ PERDEU!!')
            break
    elif opcao == 'I':
        if soma % 2 == 0:
            print('Sua opção IMPAR')
            print(f'A soma é {soma}.É PAR. VOCÊ PERDEU!!')
            break
        else:
            print('Sua opção IMPAR')
            print(f'A soma é {soma}.É IMPAR. VOCÊ GANHOU!!')
            cont = cont + 1

print('Jogo finalizado')

if cont == 0:
    print('Voce não venceu nenhuma vez')
elif cont == 1:
    print('Voce venceu uma vez')
else:
    print(f'Você venceu {cont} vezes')

