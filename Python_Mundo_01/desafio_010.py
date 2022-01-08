#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27

#Como já visto, a entrada de dados:
dinheiro = float(input('Valor em carteira: R$ '))

# Por opção, trabalhei com uma variável que seja inserido o valor da cotação.
cotacao = 3.27

dollar = dinheiro / cotacao

print('Valor em carteira: R$ {:.2f} - Valor em dóllar: US$ {:.2f}'.format(dinheiro, dollar))

#Além da calculara, há conversores disponíveis na internet que também ajudam na realização de testes.