#Faça um programa que mostre a tabuada de vários números, um de cada vez,
#para casa valor digitado pelo usuário. O programa será interrompido quando o número
# solicitado for negativo


print('Tabuada')
print('-' * 25)
c = 0
resp = 'S'
num = 0

while resp != 'N':
    num = int(input("Qual tabuada você deseja? "))
    for c in range(1, 11):
        print('{} x {} = {}'.format(num, c, (num*c)))
    print('-' * 25)
    print('-' * 25)
    resp = str(input('Deseja continuar? ')).strip().upper()
