#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e
#mostre o comprimento da hipotenusa

from math import hypot
print('Cálculo da Hipotenusa')
adjacente = float(input('Informe o cateto adjacente: '))
oposto = float(input('Informe o cateto oposto: '))

#Após a entrada dos dados, foi calculada a hipotenusa utilizando uma função da biblioteca math
hipotenusa = hypot(adjacente, oposto)

#Print na tela
print('O comprimento da hipotenusa é {:.2f} '.format(hipotenusa))

#Caso de teste: Adjacente = 9 e Oposto = 12 resulta em Hipotenusa = 15
# https://calculareconverter.com.br/calcular-hipotenusa/