type = input('''1 - 12h (AM/PM)
2 - 24h
ANYTHING ELSE - QUIT''')
  
hour = input('Digite a hora: ')

if (type == 1):
    try:
        hour = int(hour)
    except ValueError:
        print(f'Entrada inválida!')
    if hour >= 0 and hour < 12:
        print(f'Bom dia')
    elif hour > 11 and hour < 18:
        print(f'Boa tarde')
    elif hour > 17 and hour > 24:
        print(f'Boa noite')
    else:
        print(f'Hora inválida!')
elif (type == 2):
    if hour.find('am') is not -1 or hour.find('AM') is not -1:
        hour = hour.upper().split('AM')
        print(hour)
    elif hour.find('pm') is not -1 or hour.find('PM') is not -1:
        hour = hour.upper().split('PM')
        print(hour)