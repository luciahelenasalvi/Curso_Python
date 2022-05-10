#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final,
# mostre os 10 primeiros termos dessa progressão.


print('Progressão Aritmética')
print('-' * 12)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (11 - 1) * razao

for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end= ' - ')
print("Fim")