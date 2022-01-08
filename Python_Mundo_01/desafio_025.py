#Crie um programa que leia o nome de uma pessoa e diga se ele tem "Silva" no nome.

nome = input('Digite o nome de uma cidade: ').strip()

#retirar espaços iniciando pela esquerda.


print(nome[:5].upper() == 'SILVA')