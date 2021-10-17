import math

print('A kör sugara:')
x = input()


# konvertalo fv
def convert_to_number(x):
    if int(x):
        a = int(x)
        return a


def kor_terulet(r):
    return r**2 * math.pi


def kor_kerulet(r):
    return 2 * r * math.pi


# futtatas es kapcsolodo hibakazeles: ha nem számot vagy <0 számot ad meg a user

try:
    convert_to_number(x)
except ValueError:
    print(f'Error: "{x}"" nem egy szám, nem tudom a számítást elvégezni!')
else:
    if convert_to_number(x) > 0:
        print(f'A kör kerülete: {kor_kerulet(convert_to_number(x))}')
        print(f'A kör területe: {kor_terulet(convert_to_number(x))}')
    else:
        print(f'0-nál nagyobb számot kérek szépen!')
