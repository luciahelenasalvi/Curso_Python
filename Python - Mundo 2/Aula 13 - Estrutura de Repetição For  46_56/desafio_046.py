#Faça um programa que mostre na tela uma contgem regressiva para o estouro de fogos, indo de 10 ate 0,
#com pausa de 1 segundo entre eles.


import time

print('Contagem regressiva: ')

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print("FIM")
