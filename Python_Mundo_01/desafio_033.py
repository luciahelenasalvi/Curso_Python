#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Três números... ')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# Menor número:
if num1 < num2 and num1 < num3 :
    menor = num1

if num2 < num1 and num2 < num3 :
    menor = num2

if num3 < num2 and num3 < num1 :
    menor = num3

# Maior número
if num1 > num2 and num1 > num3 :
    maior = num1

if num2 > num1 and num2 > num3 :
    maior = num2

if num3 > num2 and num3 > num1 :
    maior = num3

print('Maior número: {} e Menor número: {}'.format(maior, menor))