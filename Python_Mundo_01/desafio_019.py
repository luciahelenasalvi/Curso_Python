#Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
#deles e escrevendo o nome do escolhido.
import random

print('Sorteio de alunos ')
primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))

#Criação de uma lista com os nomes dos alunos:
nomes = [primeiro, segundo, terceiro, quarto]

escolha = random.choice(nomes)
print('O aluno sorteado é: {}'.format(escolha))
