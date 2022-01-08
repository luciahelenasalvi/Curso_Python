#Escreva um programa que converte uma temperatura digitada em ºC para ºF.

# Fórmula de conversão: (Celsius x 9) / 5) + 32

print('Conversor : Celsius para Fahrenheit ')
celsius = float(input('Informe a temperatura em ºC: '))

#Aplicação da formula de conversão
conversao = ((celsius * 9) / 5) + 32

print('A temperatura de {:.1f} ºC corresponde à {:.1f} ºF'.format(celsius, conversao))

# Há conversores disponíveis na internet, muitas vezes já são disponíveis para uso na página de resultados do google.
# https://www.convertworld.com/pt/temperatura/