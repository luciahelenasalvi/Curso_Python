#Crie um programa que leia dois numeros e mostre a soma entre eles

# Para iniciar, faremos a soma com dois numeros inteiros usando a funções input (entrada de dados) e int (tipo primitivo inteiro).
# Para números reais, podemos usar float.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

# No intuito de facilitar, utilizamos a variável soma que recebe a soma de n1 e n2
soma = n1 + n2

#Agora apresentamos o resultado utilizando uma máscaram simbolizada pelas chaves {} assim como o método format,
#passando dentro dos parênteses, os parâmetros necessários.
print('A soma entre {} e {} é igual à {}'.format(n1, n2, soma))