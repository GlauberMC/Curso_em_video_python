'''
Faça um programa que leia algo pelo teclado e mostre na tela do seu
tipo primitivo e todas as informações possíveis sobre ele.
'''

info = input('Digite algo: ')
print('algo é do tipo ', type(info))
print('Só tem espaço ? ', info.isspace())
print('É um número: ', info.isnumeric())
print('É alfabético: ', info.isalpha())
print('É alfanumérico: ', info.isalnum())

