#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
#o empréstimo será negado.

print('Avaliação de Empréstimo ')

valorImovel = float(input('Informe o valor do imóvel: '))
salario = float(input('Informe o valor de salário:  '))
tempo = int(input('Informe o número de anos : '))

prestacao = valorImovel / (tempo * 12)
print('Valor da prestação: {:.2f}'.format(prestacao))

#Valor máximo de prestação:
maximo = (salario * 30) / 100
print('Valor máximo de parcela: {:.2f}'.format(maximo))

print()
print('Resultado: ')

if (prestacao <= maximo) :
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado')
