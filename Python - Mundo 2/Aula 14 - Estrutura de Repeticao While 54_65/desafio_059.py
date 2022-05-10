#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#seu programa deverá realizar a operação solicitada em cada caso.

print('Menu')
print('-' * 12)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0

#Área de Fórmulas:


while opcao != 5:
    print('Opções')
    print('''[1] Somar 
[2] Multiplicar 
[3] Maior 
[4] Novos números
[5] Sair do programa ''')
    opcao = int(input('Digite sua opção'))
    if opcao == 1:
        soma = n1 + n2
        print('Soma: {}'.format(soma))
    elif opcao == 2:
        multi = n1 * n2
        print('Multiplicação: {}'.format(multi))
    elif opcao == 3:
        if n1 > n2:
            print('Primeiro número - {} - é maior'.format(n1))
        elif n1 == n2:
            print('Ambos são iguais')
        else:
            print('Segundo número - {} - é maior'.format(n2))
    elif opcao == 4:
            print('Informe novos números')
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
            print('Encerrando programa')
    else:
        print('Opção inválida. Tente outra opção.')
print('Sair do programa')




