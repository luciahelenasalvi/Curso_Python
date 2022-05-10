#Faça um programa que leia um número inteiro e diga
#se ele é ou não um número primo.

#primo: por um e por ele mesmo.

print('Números primo')
print('-' * 12)
num = int(input('Digite um número: '))
cont = 0

for c in range(1, (num + 1)):
    if num % c == 0:
        cont = cont + 1

if cont > 2:
    print('Não é número primo')
else:
    print('É número primo')

