# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# 0 primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

print('Comparação de números')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('0 primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print ('Não existe valor maior, os dois são iguais')