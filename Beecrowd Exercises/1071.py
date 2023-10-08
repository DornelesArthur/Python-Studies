# -*- coding: utf-8 -*-

first_number = int(input())
last_number = int(input())

direction = 1
if first_number > last_number:
    direction = -1

if first_number%2 == 0:
    first_number += direction
else:
    first_number += direction*2

values_sum = 0
for value in range(first_number, last_number, direction*2):
    values_sum+=value
print(values_sum)