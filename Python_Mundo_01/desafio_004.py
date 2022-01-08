#Faça um programa que leia algo do teclado e mostre na tela  seu tipo primitivo e as possíveis afirmações sobre ele

#Como primeiro passo, a entrada do dado:
item = input('Digite uma informação: ')

#impressão do tipo primitivo: toda entrada será string por ser padrão.
print('Primeira versão do exercício: ')
print('O tipo primitivo é: ', type(item))

#Por opção pessoal, estou construindo de forma separada:
print('Somente espaços? ')
print(item.isspace())
print('É alfabético? Tem somente letras?')
print(item.isalpha())
print('É alfanumérico? Tem letras e números? ')
print(item.isalnum())
print('Todos os caracteres são minúsculas? ')
print(item.islower())
print('Todos os caracteres são maiúsculas? ')
print(item.isupper())
print('É um número? ')
print(item.isnumeric())
print('Item capitalizado? Letra maiúscula inicial?')
print(item.istitle())


#Para obter as informações, comece o print e insira a variável. Digite o ponto e 'IS'. Pronto, aparecerá
#uma lista de propriedades.


print('\n')
print('Segunda versão do exercício - Uso de format')


print('O tipo primitivo é {}'.format(type(item)))

print('Somente espaços? {}'.format(item.isspace()))

print('É alfabético? Tem somente letras? {}'.format(item.isalpha()))

print('É alfanumérico? Tem letras e números? {} '.format(item.isalnum()))

print('Todos os caracteres são minúsculas? {}'.format(item.islower()))

print('Todos os caracteres são maiúsculas? {}'.format(item.isupper()))

#não funciona com string.
print('É número? {}'.format(item.isnumeric()))

print('Item capitalizado? Letra maiúscula inicial? {}'.format(item.istitle()))
