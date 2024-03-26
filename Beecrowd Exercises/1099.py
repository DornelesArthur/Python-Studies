# -*- coding: utf-8 -*-

number_cases = int(input())

for case in range(number_cases):
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    if (n1 > n2):
        aux = n1
        n1 = n2
        n2 = aux
    if n1 % 2 == 0:
        n1 += 1
    else:
        n1 += 2
    odd_sum = 0
    for n in range(n1, n2, 2):
        odd_sum +=n
    print(odd_sum)