#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for impar, desconsidere-o

soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite um número: '))
    if (num % 2 == 0):
        soma = soma + num
        cont = cont + 1 #numeros pares
print(f'Produto dos números pares: {soma}. Foram utilizados {cont} números')
print('Fim')