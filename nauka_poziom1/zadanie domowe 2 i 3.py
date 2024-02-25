b = "pip! dwudziestu uzurpatorow dusi padalcem dwa pudle"

e = b.count('e')


print("liczba wystąpień litery e w tekście to:",e)

licznik_liter = {}

for litera in b:
    if litera.isalpha():
        if litera in licznik_liter:
            licznik_liter[litera] += 1
        else:
            licznik_liter[litera] = 1

najczestsza_litera = max(licznik_liter, key=licznik_liter.get)

print("najczesciej wystepujaca litera to:",najczestsza_litera)