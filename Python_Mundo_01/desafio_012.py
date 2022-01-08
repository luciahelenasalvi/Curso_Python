#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

#Entrada dos dados: preço do produto
preco = float(input('Preço do produto: R$ '))

#percentual de desconto que será aplicado
percentual = 5

#cálculo do valor de desconto
desconto = preco * (percentual / 100)

#cálculo do preço com o desconto
preco_final = preco - desconto

print('Preço do produto: R$ {:.2f} - Desconto: R$ {:.2f} - Preço final: R$ {:.2f}'.format(preco, desconto, preco_final))

#Cada exercício não possui uma única forma de resolução. Mas é possível calcular:
print('-'* 80)
print('Outra forma de resolução:')
preco_final = preco - (preco * (percentual / 100))
print('Preço do produto: R$ {:.2f}  - Preço final: R$ {:.2f}'.format(preco,  preco_final))
