name = input()
try:
    height = float(input())
except ValueError:
    raise ValueError('Height must be a number.')

try:
    weight = float(input())

except ValueError:
    raise ValueError('Weight  must be a number.')

imc = weight / height ** 2
print(f'{name} tem {height} de altura, pesa {weight} Kg e seu IMC é {imc}')