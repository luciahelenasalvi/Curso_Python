#Crie um programa que leia o nome completo de uma pessoa e mostre:

print('Manipulação de string')
nome = input('Informe seu nome: ')

print('Nome informado com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Nome informado com todas as letras minúsculas: {}'.format(nome.lower()))
#Neste item, aplicou-se o metodo strip, que remove espaços inúteis do início e fim da cadeia
#de caracteres
nome = nome.strip()
#itens recebe o tamanho da cadeia de caracteres, que abrange os espaços interno subtraindo
#quantos espaços em branco existem
itens = len(nome) - nome.count(" ")
print('Quantas letras temos neste nome - sem considerar espaços: {}'.format(itens))
print('Quantas letras tem o primeiro nome: {}'.format(nome.find(' ')))
print('Fim do programa')