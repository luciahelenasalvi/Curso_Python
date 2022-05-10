#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com
# a tabela abaixo:

# Abaixo de 18.5 : Abaixo de peso
# Entre 18.5 e 25 : Peso ideal
# 25 até 30 : Sobrepeso
# 30 até 40 : Obesidade
# Acima de 40 : Obesidade mórbida

print('Cálculo de IMC - Índice de Massa Corpórea')
print()
peso = float(input('Qual seu peso ? : '))
altura = float(input('Qual sua altura ? : '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC: {:.1f} - Abaixo do peso ideal'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.1f} - Peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC: {:.1f} - Sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC: {:.1f} - Obesidade'.format(imc))
else:
    print('IMC: {:.1f} - Obesidade Mórbida'.format(imc))


