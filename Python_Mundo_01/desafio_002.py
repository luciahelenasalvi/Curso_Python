#Faça um programa que leia o nome do usuário e imprima uma mensagem de boas-vindas

#Primeiro, a variável nome recebe o dado via teclado.
nome = input('Informe seu nome: ')

# Agregação de texto utilizando a vírgula.
print('É um prazer te conhecer,', nome)

print('-------------------------------------------------------------------')

#{} é uma máscara onde será impresso o nome digitado. Esta é uma saída formatada.
# Pouse o mouse sobre a variável nome, na linha de código abaixo e veja a informação de origem do dado.

print('É um prazer te conhecer, {} !'.format(nome))

