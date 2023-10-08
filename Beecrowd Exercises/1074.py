# -*- coding: utf-8 -*-

quantity = int(input())

for _ in range(quantity):
    number = int(input())
    if number == 0:
        print('NULL')
    elif (number%2 ==0):
        print('EVEN ', end='')
        if number > 0:
            print('POSITIVE')
        else:
            print('NEGATIVE')
    else:
        print('ODD ', end='')
        if number > 0:
            print('POSITIVE')
        else:
            print('NEGATIVE')
