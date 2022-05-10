#Crie um programa que mostre na tela todos os numeros pares que estão no intervalor entre 1 e 50.

print('Números no intervalo: ')

for c in range (1, 51):
    if c % 2 == 0:
       print(c, end=' ')
print('Fim')

print('Números no intervalo: ')
#com menos interação/laço:
for c in range (2, 51, 2):
    print(c, end=' ')
print('Fim')