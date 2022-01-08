#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens até 200Km e R$ 0.45 para viagens mais longas.

print('Cálculo de viagem')
quilometragem = float(input('Informe a distância em Km: '))


if (quilometragem <= 200) :
    print('Valor a ser pago: R$ {:.2f}'.format(quilometragem * 0.50))
else:
    print('Valor a ser pago: R$ {:.2f}'.format(quilometragem * 0.45))
print('Fim')

print('\n')
print('Cálculo de viagem :  V2')
quilometragem = float(input('Informe a distância em Km: '))


if (quilometragem <= 200) :
    preco = quilometragem * 0.50
    print('Valor a ser pago: R$ {:.2f}'.format(preco))
else:
    preco = quilometragem * 0.45
    print('Valor a ser pago: R$ {:.2f}'.format(preco))
print('Fim')