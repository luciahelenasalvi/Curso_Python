#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# 1 para binário; 2 para octal;  3 para hexadecimal.

print('Conversão de Base')
numero = int(input('Informe um número: '))
print('Bases para conversão')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
base = int(input('Informe a base de conversão: '))

#fatiamento de string.
if (base == 1):
    print('Você escolheu conversão binária')
    print('O número {} em binário é: {}'.format(numero, bin(numero)[2:]))
elif (base == 2):
    print('Você escolheu conversão octal')
    print('O número {} em octal é: {}'.format(numero, oct(numero)[2:]))
elif (base == 3):
    print('Você escolheu conversão hexadecimal')
    print('O número {} em binário é: {}'.format(numero, bin(numero)[2:]))
else:
    print ("O número digitado não equivale a nenhuma opção possível")