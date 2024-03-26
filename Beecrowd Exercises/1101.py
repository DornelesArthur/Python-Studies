# -*- coding: utf-8 -*-

while True:
    m, n = input().split()
    m = int(m)
    n = int(n)
    if (n <= 0 or m <= 0):
        break

    if m > n:
        m,n = n,m

    numbers_sum = 0
    for number in range(m, n+1):
        print(number, end=' ')
        numbers_sum+=number
    print(f'Sum={numbers_sum}')