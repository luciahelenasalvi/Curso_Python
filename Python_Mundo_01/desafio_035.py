#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Condições para um triângulo: ')
segA = float(input('Informe o segmento A: '))
segB = float(input('Informe o segmento B: '))
segC = float(input('Informe o segmento C: '))



if segA < segB + segC and segB < segA + segC and segC < segA + segB :
    print('Os seguimentos cumprem condição para formação de um triângulo')
else:
    print('Os seguimentos não cumprem condição para formação de um triângulo')


#Fonte: Condição parhttps://slideplayer.com.br/slide/9767614/