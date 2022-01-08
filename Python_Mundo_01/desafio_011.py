#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

#Entrada dos dados - altura e largura da parede para cálculo de área (metros quadrados)
altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

#fórmula do cálculo de área
area = altura * largura

#na variável, o rendimento de 1 litro de tinta.
rendimento = 2

#calculo de tinta necessária: área total dividido pelo rendimento de cada litro.
tinta = area / rendimento

print('Área total: {} m2 - Quantidade de tinta: {} litros'.format(area, tinta))
