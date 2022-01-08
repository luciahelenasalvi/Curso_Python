#Faça um programa que leia um número inteiro e mostre na sua tela o seu antecessor e seu sucesso.

#Passo 1: Leitura do dado de entrada.
numero = int(input('Informe um número: '))

#Quem é meu antecessor e meu sucessor?

# Antecessor é o número menos 1, ou seja, considerando o número 9 meu antecessor é 8, ou 9 - 1.
antecessor = numero - 1

# Sucessor é o número mais 1, ou seja, considerando o número 9 meu sucessor é 10, ou 9 + 1.
sucessor = numero + 1

print('\n')
print('Número escolhido: {} \n'
      'Antecessor: {} \n'
      'Sucessor: {}'.format(numero, antecessor, sucessor))

#Em geral, utilizo variáveis, pois elas tornam mais claras na minha percepção:
print('\n')
print('Segunda versão: ')
print('Número escolhido: {}, Antecessor: {} e Sucessor: {}'.format(numero, (numero-1), (numero+1)))
