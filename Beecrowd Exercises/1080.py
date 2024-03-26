# -*- coding: utf-8 -*-

highest = None
h_position = 0
for position in range(1,101):
    value = int(input())
    if (highest == None or highest < value):
        highest = value
        h_position = position
print(highest)
print(h_position)