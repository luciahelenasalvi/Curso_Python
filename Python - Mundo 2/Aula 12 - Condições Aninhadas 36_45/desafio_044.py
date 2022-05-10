# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento.

# à vista dinheiro/cheque : 10% de desconto
# à vista cartão : 5% de desconto
# em até 2x no cartão : preço normal
# 3 x ou mais no cartão : 20% de juros

print('Valor do produto ')
valor = float(input('Valor do produto: '))
print()
print('Condição de pagamento: ')
print('(1) à vista dinheiro/cheque')
print('(2) à vista cartão')
print('(3) até 2x no cartão')
print('(4) 3x ou mais no cartão')
forma = int(input('Escolha a forma de pagamento: '))

if forma == 1:
    preco = valor - ((valor * 10) /100)
    print('Preço final: {:.2f}'.format(preco))
elif forma == 2:
    preco = valor - ((valor * 5) /100)
    print('Preço final: {:.2f}'.format(preco))
elif forma == 3:
    print('Preço final: {:.2f}'.format(valor))
elif forma == 4:
    preco = valor + ((valor * 20) /100)
    print('Preço final: {:.2f}'.format(preco))
else:
    print('Opção inválida')