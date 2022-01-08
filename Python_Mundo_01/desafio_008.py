#Escreva um programa que leia um valor em metros e o exiba convertido em centimentos e milímetros

metro = float(input('Medida em metros: '))

#1 metros = 100 centímetros
centimetros = metro * 100

#1 metros = 1000 milímetros
milimetros = metro * 1000

print('{:.1f} metros equivalem à {:.1f} centímetros(cm) e {:.1f} milímetros (mm)'.format(metro, centimetros, milimetros))