# -*- coding: utf-8 -*-

quantity = int(input())

quantity_in = 0
for _ in range(quantity):
    number = int(input())
    if number in range(10,21):
        quantity_in+=1

print(f'{quantity_in} in')
print(f'{quantity-quantity_in} out')