# napisz program, który przyjmuje numer i zwraca wszystkie dostępne informacje
# napisz program, który przyjmuje imię i zwraca stan konta

imiona = {
    4123: 'Kamil',
    1234: 'Asia',
    8777: 'Bartosz'
}

stan_konta = {
    4123: 520,
    1234: 0,
    8777: 100000
}

for number in imiona.keys():
    print(imiona[number])

for value in imiona.values():
    print(value)


