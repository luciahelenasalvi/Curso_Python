#Faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('Validação de entrada de dados')
print('-' * 12)
sexo = str(input('Informe o sexo: ')).strip().upper()

while sexo not in 'MmFf':
    print('Valor invalido. Digite M ou F.')
    sexo = str(input('Por favor, informe um valor válido ')).strip().upper()[0]
print('Valor correto para esta opção')