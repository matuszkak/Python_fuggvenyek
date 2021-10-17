names = [
    'Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter',
    'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs',
    'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint'
]

# , 'Kovács Tamás'


# csoport kiiratas kepernyore fv
def list_print(list_no, list):
    print(f'  {list_no}. csoport:')
    for i in range(0, len(list)):
        print(list[i])


# sorbarendezes
sorted_names = sorted(names)
# print(sorted_names)

# csoport letszam meghatarozas - paratlan fo eseten az elso csoportban lesznek tobben
csop = round(len(sorted_names) / 2)

# csoportba sorolas
group1 = sorted_names[:csop]
group2 = sorted_names[csop:]

list_print(list_no=1, list=group1)
list_print(list_no=2, list=group2)
