#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
#o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
#digitados e qual foi a soma entre eles (desconsiderando a flag)



print('Condição de Parada - Sem break')
print('-' * 12)
soma = 0
cont = 0
num = 0

while num != 999:
    num = int(input('Digite um número: '))
    soma = soma + num
    cont = cont + 1
contador = cont - 1
total = soma - 999
print('Números digitados: {}  Produto: {}'.format(contador, total))

