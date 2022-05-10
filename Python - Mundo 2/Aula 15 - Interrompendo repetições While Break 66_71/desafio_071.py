#Crie um programa que simule o funcionamento de um caixa eletronico. No início, pergunte
#ao usuário qual será o valor sacado (numero inteiro) e o programa vai informar quantas cédulas
# de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de 50, 20, 10 e 1 real.

print('Caixa Eletônico')
print('-' * 28)
notas = [50, 20, 10, 1]


valor = int(input('Quanto deseja sacar? '))


for i in range(4):
    num = valor//notas[i]
    print('Notas de {} : {}'.format(notas[i], num))
    valor = valor - (num * notas[i])

