def is_integer(number):
    if isinstance(number, str):
        try:
            return(is_integer(float(number)))
        except ValueError:
            return False
    elif isinstance(number, float):
        try:
            return(is_integer(int(number)))
        except ValueError:
            return False
    elif isinstance(number,int):
        return True
    else:
        return False

number = input('Digite um número inteiro: ')

if is_integer(number):
    if (int(number) % 2 == 0):
        print(f'Par')
    else:
        print(f'Impar')
else:
    print(f'Não é um número inteiro')

