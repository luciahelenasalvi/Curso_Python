#Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
#no final do programa, mostre:
#a media de idade do grupo.
#qual é o nome do homem mais velho
#quantas mulheres tem menos de 20 anos.

print('Estatística de cadastro')
print('-' * 12)
somaIdade = 0
cont = 0

for cad in range(1,5):
    print('------- {}ª pessoa ------'.format(cad))
    nome = str(input('Informe o nome:  ')).strip()
    idade = int(input('Informe a idade:  '))
    somaIdade = somaIdade + idade
    sexo = str(input('Informe o sexo [M/F]: ')).strip()
    if idade <= 20 and sexo == 'F':
        cont = cont + 1


media = somaIdade/4

print('Média de idade do grupo: {}'.format(media))
print('Número de mulheres até 20 anos no grupo: {} de 4 inserções'.format(cont))