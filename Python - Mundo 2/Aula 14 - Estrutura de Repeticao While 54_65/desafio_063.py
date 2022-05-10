#Escreva um programa que leia um numero n inteiro qualquer e mostre nas telas os n primeiros
# elementos de uma sequencia de Fibonacci
#Ex: 0-1-1-2-3-5-8

print('Sequencia de Fibonacci')
print('-' * 12)
num = int(input('Informe um número inteiro (2, 3, 5...) : '))

n1 = 0
n2 = 1
n3 = n1 + n2
cont = 3

if num == 1:
    print('1ª termo:  {}'.format(n1))
elif num == 2:
    print('2ª termo: {}'.format(n2))
elif num == 3:
    print('3ª termo: {}'.format(n3))
elif num > 3:
    cont = 3
    while cont != num:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        cont = cont + 1
    print('{}ª termo: {}'.format(cont, n3))
print('Fim')
