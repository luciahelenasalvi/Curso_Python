#Crie um algoritmo que leia um número e mostre o dobro, o triplo e a raiz quadrada

#Leitura de um número inteiro
numero = int(input('Digite um número inteiro: '))

#O dobro de um número é o número multiplicado por 2
dobro = numero * 2

#O triplo de um número é o número multiplicado por 3
triplo = numero * 3

#A raiz pode ser obtida pela multiplicação do número por (1/2). Raiz cúbica pode ser multiplicado por (1/3)
raiz = numero ** (1/2)

#{:.2f} trabalha a máscara para uso de duas casas decimais. No caso de rais quadrada, sempre retorna dado tipo float.
print('Número: {} - Dobro: {} - Triplo: {} - Raiz quadrada: {:.2f}'.format(numero, dobro, triplo, raiz))