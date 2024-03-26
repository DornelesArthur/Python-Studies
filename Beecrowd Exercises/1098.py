# -*- coding: utf-8 -*-

i = 0.0
j_values = [1, 2, 3]

while i <= 2:
    for index, j in enumerate(j_values):
        if i.is_integer():
            print('I={:.0f} J={:.0f}'.format(i,j+i))
        else:
            print('I={:.1f} J={:.1f}'.format(i,j+i))
    i = round(i+0.2,1)
    