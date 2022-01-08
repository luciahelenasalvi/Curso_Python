#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
from  datetime import date
print('Ano Bissexto')
ano = int(input('Informe o ano ou O para o ano atual:  '))
if ano == 0 :
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('{} é ano bissexto'.format(ano))
else:
    print('{} não é ano bissexto'.format(ano))
print('Fim')