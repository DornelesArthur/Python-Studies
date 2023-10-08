# -*- coding: utf-8 -*-

number = int(input())

for even_number in range(2, number+1, 2):
    print(f'{even_number}^2 = {even_number**2}')
