#Crie um programa que leia um número real  qualquer pelo teclado e mostre na tela a sua porção inteira.
#Por exemplo: digite o número 6.127. Este número tem a parte inteira 6.


#Neste caso, foi utilizado o import da funcionalidade trunc.
from math import trunc
print('Verificação de parte inteira')

numero = float(input('Digite um número real: '))
#Se usar import math, é preciso inserir math.trunc(numero)
print('Parte inteira de {:.3f} é {}'.format(numero, trunc(numero)))

