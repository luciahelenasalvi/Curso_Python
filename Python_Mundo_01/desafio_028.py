#Escreva um programa que faça o computador "pensar" emn um número inteiro #entre 0 e 5 e peça para o usuário tentar
# descobir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep

print('== Jogo de Advinhação ==')
numero = random.randrange(0, 6)
#Outra forma: numero = randint(0

#Para digitar o número correto, faça o print do resultado da randomização.
#print(numero)

aposta = int(input('Digite um número '))
print('Processando....')
sleep(3)
if (numero == aposta) :
    print('Você acertou!! É o número {}'.format(numero))
else:
    print('Você não acertou. O número é {} e você digitou {}'.format(numero, aposta))

print('FIM')





