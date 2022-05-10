#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#Se ele ainda vai se alistar ao serviço militar, se é a hora de ele se alistar ou se já passou do tempo do alistamento
#Seu programa também deverá mostra o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year

print('Alistamento Militar')
ano = int(input('Ano de nascimento: '))

idade = ano_atual - ano

print('Idade: {}'.format(idade))

if idade == 18:
    print('Você deve se alistar imediatamente')

elif idade < 18:
    tempo = 18 - (idade)
    print('Ainda falta {} ano(s) para seu alistamento'.format(tempo))

elif idade > 18:
    tempo = idade - 18
    print('Voce deveria ter se alistado {} anos do alistamento'.format(tempo))