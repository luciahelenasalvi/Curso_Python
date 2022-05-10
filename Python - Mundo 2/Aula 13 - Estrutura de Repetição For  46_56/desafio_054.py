#Crie um programa que leia o ano de nascimento de sete pessoas.
#no final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores


from datetime import date

contMaior = 0
contMenor = 0

print('Maiores e menores')
data_atual = date.today()

for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    if data_atual.year - ano > 18 or data_atual.year - ano == 18:
        contMaior = contMaior + 1
    else:
        contMenor = contMenor + 1

print('Maiores de idade: {}'.format(contMaior))
print('Menores de idade: {}'.format(contMenor))