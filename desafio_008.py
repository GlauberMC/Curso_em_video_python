'''
Escreva um programa que leia um valor em metros e o exiba convertido
em centímetros e milímetros.
'''

num = int(input('Digite um número correspondente em metros: '))

km = num / 1000
hm = num / 100
dam = num / 10
dm = num * 10
cm = num * 100
mm = num * 1000

print(f'{km} km')
print(f'{hm}  hm')
print(f'{dam}   dam')
print(f'{dm}    dm')
print(f'{cm}   cm')
print(f'{mm}  mm')

