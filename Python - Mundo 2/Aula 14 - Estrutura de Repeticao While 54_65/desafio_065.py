#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
# a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.



print('Média e Maior&Menor')
print('-' * 12)
soma = 0
cont = 0
num = 0
resp = 'S'
menor = 0
maior = 0

while resp != 'N':
    num = int(input('Digite um número: '))
    soma = soma + num
    resp = str(input('Deseja continuar? S ou N ')).strip().upper()
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont = cont + 1

media = soma / cont
print('Média: {}   Maior valor: {}    Menor valor: {}'.format(media, maior, menor))