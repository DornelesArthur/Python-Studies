name = input()
age = input()

if name and age:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')
    print(f'Seu nome{" " if " " in name else " não"} contém espaços.')
    print(f'Seu nome tem {len(name)} letras')
    print(f'A última letra do seu nome é {name[-1]}')
else:
    print('Desculpe, você deixou campos vazios')

