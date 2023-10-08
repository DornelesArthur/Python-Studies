# -*- coding: utf-8 -*-
quantity = int(input())

operators = ['+','-','*','/','^','(',')']

for _ in range(quantity):
    operators_stack = [];
    vars_stack = [];
    expression = input()
    for symbol in expression:
        if symbol in operators:
            operators_stack.append(symbol)
        else:
            vars_stack.append(symbol)
    print(operators_stack)
    print(vars_stack)