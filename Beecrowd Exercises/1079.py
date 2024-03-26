# -*- coding: utf-8 -*-

number = int(input())
for case in range(number):
    n1, n2, n3 = input().split()
    average = (float(n1)*2 + float(n2)*3 + float(n3)*5)/10
    print(round(average,1))
    