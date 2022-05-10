#Crie um programa que leia uma frase qualquer e diga se ela
#é um palindromo, desconsiderando os espaços.

print('Palíndromos')
print('-' * 12)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)  ## desconsidera espaços
print('Você digitou {}'.format(junto))

inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')


    #Frases para teste:
    # apos a sopa
    # a sacada da casa
    # a torre daderrota
    # o lobo ama o bolo
    # anotaram a data da maratona

