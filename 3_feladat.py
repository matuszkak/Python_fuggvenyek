print('Adj meg egy számot:')
x = input()


# konvertalo fv
def convert_to_number(x):
    if int(x):
        a = int(x)
        return a


# kiirato fv
def print_hello(count):
    for i in range(1, count + 1):
        print(f'{i}. Helló!')


# futtatas es kapcsolodo hibakazeles
try:
    print_hello(convert_to_number(x))
except ValueError:
    print(f'Error: "{x}"" nem egy szám!')
