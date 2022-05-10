#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
#acordo com a média atingida:

# Média abaixo de 5.0 = Reprovado
# Média entre 5.0 e 6.9 = Recuperação
# Média 7.0 ou superior = Aprovado

print('Cálculo de Média de Notas')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média é {:.1f}. Você foi reprovado'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média é {:.1f}. Você está em recuperação'.format(media))
else:
    print('Sua média é {:.1f}. Você foi aprovado'.format(media))
