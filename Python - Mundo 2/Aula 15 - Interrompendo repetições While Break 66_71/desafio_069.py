#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#o programa deverá perguntar se o usuário querou não quer continuar. No final, mostre:
#Quantas pessoas tem mais de 18 anos.
#Quantos homens foram cadastrados.
#Quantas mulheres tem menos de 20 anos

print('Estatísticas...')
print('-' * 25)
resp = 'S'
contIdade = 0
contHom = 0
cont = 0
while resp != 'N':
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
    resp = str(input('Deseja realizar um novo cadastro? [S/N]  ')).strip().upper()

if idade > 18:
    contIdade = contIdade + 1
if sexo == 'M':
    contHom = contHom + 1
if sexo == 'F' and idade < 20:
    cont = cont + 1

#Quantas pessoas tem mais de 18 anos.
#Quantos homens foram cadastrados.
#Quantas mulheres tem menos de 20 anos
print(f'Foram cadastradas {contIdade} pessoas com mais de 18 anos')
print(f'No cadastro, foram registrados {contHom} pessoas do sexo masculino')
print(f'Também há {cont} pessoas do sexo feminino com menos de 20 anos de idade')