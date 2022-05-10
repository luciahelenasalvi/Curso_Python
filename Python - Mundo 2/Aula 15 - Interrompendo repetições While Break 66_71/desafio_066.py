#Crie um programa que leia vários números inteiros pelo teclado. O programa
# vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles desconsiderando a flag.


cont = 0
num = 0
soma = 0

while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'Produto: {soma}  _________  Números digitados: {cont}')