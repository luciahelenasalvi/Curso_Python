#Faça um programa que leia um número qualquer e mostre na tela sua tabuada.

num = int(input('Digite um número: '))

print('Tabuada do {}'.format(num))
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' * 12)

#{:2} : esta mascara foi utilizada para espaçamento regular do campo obtendo efeito visual.

#print('-' * 12) resulta numa linha com 12 traços. É, de fato, uma multiplicação de string.