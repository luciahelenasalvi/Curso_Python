#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
#se o usuário vai continuar. No final, mostre:
#Qual é o total gasto na compra;
#Quantos produtos custam mais de R$ 1000
#Qual é o nome do produto mais barato


print('Lista de Compras : Mercado')
print('-' * 28)
resp = 'S'
menor = 10000
contProdutos = 0
contPreco = 0
prod = []

while resp != 'N':
    nome = str(input('Informe o nome do produto: '))
    preco = int(input('Informe o preço: '))
    #Produto com menor preço
    if preco < menor:
        menor = preco
        prod = []
        prod.append(nome)
        prod.append(preco)
    #Produtos > 1000
    if preco > 1000:
        contPreco = contPreco + 1
    #Total da compra
    contProdutos = contProdutos + preco
    resp = str(input('Deseja realizar um novo cadastro? [S/N]  ')).strip().upper()

print(f'Total gasto: {contProdutos}')
print(f'Número de produtos com valor acima de R$ 1000: {contPreco}')
print(f'Produto com menor preço: {prod[0]}  Valor: {prod[1]}')