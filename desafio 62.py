#! /usr/bin/python3.6

print(
'''Refaça o desafio 51, lendo o primeiro
termo e a razão da PA, mostrando os 10
primeiros termos da progressão usando a
estrutura while.
'''
)

a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
i = 10
while(i != 0):
    print(a, '-', end = ' ')
    a += r
    i -= 1
    if i == 0:
        print('\b\b')
        i = int(input('Quantos termos extras? '))
