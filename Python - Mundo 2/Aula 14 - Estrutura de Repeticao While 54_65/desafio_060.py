#Faça um programa que leia um número qualquer e mostre o seu fatorial
#ex. 5! = 5 x 4 x 3 x 2 x 1 = 120.



multi = 1
print('Fatorial')

num = int(input('Digite um número: '))

for c in range (-1,  num, -1):
    multi = multi * c;
print('Fatorial de {} é {}'.format(num, multi))


print('-' * 12)
print('Fatorial')
num = int(input('Digite um número: '))
cont = num
multi = 1

while cont != 0:
    multi = multi * cont;
    cont = cont - 1
print('Fatorial de {} é {}'.format(num, multi))

