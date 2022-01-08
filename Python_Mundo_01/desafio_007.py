#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.

# Utilizo float por se tratar de claculos que podem resultar em números de ponto flutuante
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#A fórmula deve observar a ordem de precedência, pois é necessário que se realize a soma antes da divisão.
media = (nota1 + nota2) / 2

print('Nota 1: {} - Nota 2: {} - Média: {:.1f}'.format(nota1, nota2, media))

#Cuidado. Com 1 casa após a vírgula, há o arredondamento para cima (ceil).