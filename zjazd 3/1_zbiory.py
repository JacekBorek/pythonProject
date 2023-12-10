zbior1 = {1, 4, 5, 4, 2, 7}
zbior2 = {2, 7, 8, 0, 9}

print(zbior1)
print(zbior2)

# suma zbiorów -> |
# część wspólna -> &
# różnica -> -
# różnica symetryczna (bez części wspólnej) -> ^

print(f'Suma zbiorów: \n{zbior1 | zbior2}')
print(f'część wspólna: \n{zbior1 & zbior2}')
print(f'różnica: \n{zbior1 - zbior2}')
print(f'różnica symetryczna: \n{zbior1 ^ zbior2}')

lista = [1, 2, 4, 4, 56, 7, 7, 0, 9, 7]

lista = list(set(lista))
print(lista)

imiona = {'Jacek', 'Paulina', 'Zdzisiu', 'Romuald', 'Zosia'}
# stworzyć 2 zbiory osobny dla kobiet i osobny dla mężczyzn


kobiety = set()
mezczyzni = set()

for imie in imiona:
    if imie[-1] == 'a':
        kobiety.add(imie)
    else:
        mezczyzni.add(imie)
print('imiona żeńskie', kobiety)
print('imiona męskie', mezczyzni)