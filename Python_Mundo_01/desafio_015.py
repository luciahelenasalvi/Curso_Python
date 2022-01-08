#Escreva um programa que pergunte a quantidade de Km percorridos por um carro e a
#quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar sabendo
#que o carro custa R$60 reais por dia e R$ 0.15 por Km rodado.

print('Cálculo do valor do aluguel de veículo: ')
dias = int(input('Quantos dias de aluguel? '))
quilometragem = float(input('Quantos Km foram rodados? '))

#Calcula-se o valor dos dias e da quilometragem
preco = (dias * 60.00) + (quilometragem * 0.15)

print('Preço da estadia: R$ {:.2f}'.format(preco))
