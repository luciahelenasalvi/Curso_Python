#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

print('Par ou Ímpar?')
numero = int(input('Digite um número: '))

if (numero % 2 == 0) :
    print('O número {} é Par'.format(numero))
else:
    print('O número {} é Ímpar'.format(numero))
print('Fim')

