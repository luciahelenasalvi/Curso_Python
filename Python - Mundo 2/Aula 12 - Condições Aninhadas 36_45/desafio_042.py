#Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais;
# Isóceles: dois lados iguais;
# Escaleno: todos os lados diferentes

print('Condições para um triângulo: ')
segA = float(input('Informe o segmento A: '))
segB = float(input('Informe o segmento B: '))
segC = float(input('Informe o segmento C: '))

if segA < segB + segC and segB < segA + segC and segC < segA + segB :
    print('Os seguimentos cumprem condição para formação de um triângulo')
    if segA == segB == segC:
        print('Trata-se de um triângulo equilátero')
    elif segA != segB != segC != segA:
        print('Trata-se de um triângulo escaleno')
    else:
        print('Trata-se de um triângulo isóceles')
else:
    print('Os seguimentos não cumprem condição para formação de um triângulo')
