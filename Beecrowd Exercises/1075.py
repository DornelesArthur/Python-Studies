# -*- coding: utf-8 -*-

divider = int(input())

for number in range(10000):
    if number%divider == 2:
        print(number)
