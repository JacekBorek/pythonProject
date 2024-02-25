#funkcja ktora przyjmuje wiek auta, liczbę szkód, wiek kierowcy
#funkcja mowi ile będzie kosztować składka na ubezpieczenie

def koszt_skladki(rok, szkoda, wiek):

    skladka = 0
    skladka += rok * 20
    skladka += szkoda * 200
    if wiek < 25:
        skladka += 100
    # print(f'skladka wynosi {skladka}')
    return skladka

skladka = koszt_skladki(10,2,26)
# print(skladka)

czynsz = 500
jedzenie = 700
koszt_zycia = czynsz + jedzenie + skladka

print(f'Koszty życia to {koszt_zycia}, w tym składka to {skladka}')
print('---------------')

imie = 'Jacek'
if len(imie) > 5:
    print(f"{imie} masz długie imię")
else:
    print(f'{imie} masz krótkie imię')

wiek_auta = int(input('podaj wiek auta \n'))
szkoda = int(input('ile razy rozwaliles/as auto \n'))
wiek_kierowcy = int(input('Twoj wiek \n'))

if koszt_skladki(wiek_auta,szkoda,wiek_kierowcy) > 1000:
    print('nie stać cie')
else:
    print('koszt akceptowalny')