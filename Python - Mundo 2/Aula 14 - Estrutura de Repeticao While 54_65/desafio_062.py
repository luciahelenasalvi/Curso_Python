# Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O
# programa encerra quando ele quer mostrar 0 termos.

print('Progressão Aritmética')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
# Inicialização com 1 : 1º termo via teclado
cont = 1
soma = primeiro
termo = 1

print('{}'.format(primeiro), end=' - ') #primeiro termo

while cont < 10:
    soma = soma + razao
    print('{}'.format(soma), end=' - ')
    cont = cont + 1
    termo = termo + 1
    print("", end="")
resp = int(input('Quantos termos deseja acrescentar? '))

while resp != 0:
    contador = 0
    while contador != resp:
        soma = soma + razao
        print('{}'.format(soma), end=' - ')
        contador = contador + 1
        termo = termo + 1
        print("", end="")
    resp = int(input('Quantos termos deseja acrescentar? '))
print('Fim')

print('Progressão finalizada com {} termos!'.format(termo))
