#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 km/h, mostre a mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite.

print('Multa de trânsito')
velocidade = int(input('Velocidade do veículo: '))

valor = (velocidade - 80) * 7.00

if velocidade > 80 :
    print('Multa imposta no valor de R$ {:.2f}'.format(valor))
else:
    print('Não ocorrência de multa')
print('Fim')