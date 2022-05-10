#Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10.
#Só que agora o jogado vai tentar advinhar ate acertar, mostrando no final quantos palpites foram
#necessários para vencer.

import random
from time import sleep
cont = 1

print('== Jogo de Advinhação ==')
print('-' * 12)
numero = random.randint(0, 25)

print('O computador escolheu um número ')

aposta = int(input('Digite sua aposta: '))
print('Processando....')
sleep(3)

while numero != aposta:
    print('Você não acertou.')
    cont = cont + 1

    if numero > aposta:
        aposta = int(input('Tente outra vez... Digite um numero maior... '))
    if numero < aposta:
        aposta = int(input('Tente outra vez... Digite um numero menor... '))

print('Você acertou com {} lances!! É o número {}'.format(cont, numero))

print('FIM')
