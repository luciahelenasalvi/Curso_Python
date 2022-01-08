#Crie um programa que leia o nome de uma cidade e diga se ela
#começa ou não com a palavra "Santo"

cidade = input('Digite o nome de uma cidade: ').strip()

#retirar espaços iniciando pela esquerda.
cidade.lstrip()

print(cidade[:5].upper() == 'SANTO')


