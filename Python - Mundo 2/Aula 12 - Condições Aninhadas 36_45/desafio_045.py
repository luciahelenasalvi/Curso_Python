#Crie um programa que faça o computador jogar Jokenpô com você (Pedra/ Papel/ Tesoura)
import random

print('JOKENPÔ')
print('Suas opções: ')
print(' ( 1 ) Pedra')
print(' ( 2 ) Papel')
print(' ( 3 ) Tesoura')
jogador = int(input('Qual sua opção ? '))

opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = random.choice(opcoes)
print('Computador: {}'.format(computador))

if jogador == 1:
    print('Sua escolha é Pedra')
    if computador == 'Pedra':
        print('Escolha do computador é Pedra. Deu empate')
    elif computador == 'Papel':
        print('Escolha do computador é Papel. Papel embrulha pedra')
    elif computador == 'Tesoura':
        print('Escolha do computador é Tesoura. Pedra quebra tesoura')
elif jogador == 2:
    print('Sua escolha é Papel')
    if computador == 'Pedra':
        print('Escolha do computador é Pedra. Papel embrulha Pedra')
    elif computador == 'Papel':
        print('Escolha do computador é Papel. Deu empate')
    elif computador == 'Tesoura':
        print('Escolha do computador é Tesoura. Tesoura corta Papel')
elif jogador == 3:
    print('Sua escolha é Tesoura')
    if computador == 'Pedra':
        print('Escolha do computador é Pedra. Pedra quebra Tesoura')
    elif computador == 'Papel':
        print('Escolha do computador é Papel. Tesoura corta papel')
    elif computador == 'Tesoura':
        print('Escolha do computador é Tesoura. Deu empate')
else:
    print('Opção não existe')





