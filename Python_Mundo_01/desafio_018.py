#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math
print('Funções Trigonométricas')
angulo = float(input('Informe o ângulo: '))

# As funções utilizam o valor em radianos, por isso, é preciso fazer a conversão.
radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print('Seno: {:.2f} -  Cosseno: {:.2f} - Tangente: {:.2f}'.format(seno, cosseno, tangente))
