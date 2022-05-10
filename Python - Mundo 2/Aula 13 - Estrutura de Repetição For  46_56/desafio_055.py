#Faça um programa que leia o peso de cinco pessoas.
#no final, mostre qual foi o maior e o menor peso lidos.

import numpy
print('Maior e menor peso')
print('-' * 12)
maior = 0
menor = 0

for p in range(1, 6):
    peso = (float(input('Digite o peso da {}ª pessoa:'.format(p))))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print('Maior peso: {}'.format(maior))
print('Menor peso {}'.format(menor))
