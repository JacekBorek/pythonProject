def przywitaj():
    print('--------------')
    print('Witamy na spotkaniu')
    print('plik z logami uaktualniony')

def przywitaj_spersonalizowane1(x):
    print('Siema', x)
    print(f'Siema {x}')


while True:
    decision = input('czy przywitać? T/N: \n')

    if decision.lower() == 't':
        przywitaj()
    else:
        print('Żegnamy')
        break

imię = input('Podaj imię: \n')
przywitaj_spersonalizowane1(imię)
print('--------')
przywitaj_spersonalizowane1('Jacek')