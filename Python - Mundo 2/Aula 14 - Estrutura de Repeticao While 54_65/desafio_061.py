#Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
#termos da progressão usando a estrutura while


print('Progressão Aritmética')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
soma = primeiro

print('{}'.format(primeiro), end=' - ')

while cont < 10:
    soma = soma + razao
    print('{}'.format(soma), end=' - ')
    cont = cont + 1
print("Fim")