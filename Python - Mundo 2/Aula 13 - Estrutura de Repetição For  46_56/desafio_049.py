#Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher,
#so que agora utilizando um laço for.

num = int(input('Digite um número: '))

print('Tabuada do {}'.format(num))
print('-' * 12)

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('-' * 12)
