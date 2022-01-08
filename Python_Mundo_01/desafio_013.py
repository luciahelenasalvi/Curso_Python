#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario, com 15% de aumento

#Entrada dos dados: salário
salario = float(input("Salário do funcionário: R$ "))

#Variável que recebe o percentual de desconto.
percentual = 15

#Cálculo do valor de aumento
aumento = salario * (percentual / 100)

#Cálculo do valor final do salário, considerando o aumento proposto.
salario_final = salario + aumento

print('Salario: R$ {:.2f} - Aumento: R$ {:.2f} - Salario com aumento: R$ {:.2f}'.format(salario, aumento, salario_final))

print('-' * 80)
print('Outra forma de resolução: ')
#Cálculo do valor final do salário, considerando o aumento proposto.
salario_final = salario + (salario * (15 / 100))
print('Salario: R$ {:.2f} - Salario com aumento: R$ {:.2f}'.format(salario, salario_final))