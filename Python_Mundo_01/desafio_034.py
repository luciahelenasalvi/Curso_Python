#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento para salarios superiores
# à R$ 1.250.00, calcule aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

print('Cálculo de novo salário')
salario = float(input('Informe o salário do funcionário: R$ '))

if (salario <= 1250.00) :
    novo_salario = salario + (salario * (15 / 100))
else:
    novo_salario = salario + (salario * (10 / 100))

print('Valor: R$ {:.2f}'.format(novo_salario))