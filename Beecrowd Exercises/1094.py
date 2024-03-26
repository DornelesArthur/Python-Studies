# -*- coding: utf-8 -*-

number_cases = int(input())

animals_count = {
    "C":0,
    "R":0,
    "S":0,
}
animals_total = 0
for x in range(number_cases):
    number_animals, animal_type = input().split()
    animals_count[animal_type] += int(number_animals)
    animals_total += int(number_animals)

print(f'Total: {animals_total} cobaias')
print(f'Total de coelhos: {animals_count["C"]}')
print(f'Total de ratos: {animals_count["R"]}')
print(f'Total de sapos: {animals_count["S"]}')
print('Percentual de coelhos: {:.2f} %'.format(round(animals_count["C"]/float(animals_total)*100,2)))
print('Percentual de ratos: {:.2f} %'.format(round(animals_count["R"]/float(animals_total)*100,2)))
print('Percentual de sapos: {:.2f} %'.format(round(animals_count["S"]/float(animals_total)*100,2)))
