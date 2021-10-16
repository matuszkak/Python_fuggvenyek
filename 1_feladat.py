# a fv kilistázza azokat a szamokat egy adott tartomanyon belul, amelyek oszthatoak egy adott szammal, de nem oszthatoak egy megadott masikkal


def oszthatosag_vizsgalat(start, finish, oszthato, nem_oszthato):

    szamsor = []
    for num in range(start, finish + 1):
        if num % oszthato == 0 and num % nem_oszthato != 0:
            szamsor.append(num)

    return szamsor


print(
    oszthatosag_vizsgalat(start=2000,
                          finish=3200,
                          oszthato=1,
                          nem_oszthato=1235452))
