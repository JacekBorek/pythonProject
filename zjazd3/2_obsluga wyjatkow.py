while True:
    try:
        wiek = int(input('Podaj liczbę: \n'))
        x = 5 / 0
        break
    except ValueError:
        print('źle, jeszcze raz podaj wiek: ')
    except ZeroDivisionError:
        x = 0
        break

print(f'na emeryture przejdziesz za: {65 - wiek}')