#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
#leia o nome de quatro alunos e mostre a ordem sorteada.

import random

print('Ordem de apresentação dos alunos: ')
primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))

nomes = [primeiro, segundo, terceiro, quarto]
random.shuffle(nomes)
print('A ordem de apresentação será:')
print(nomes)

