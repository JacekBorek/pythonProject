# slownik_imion = {
#     'Jacek': 'Jack',
#     'Maria': 'Marry',
#     'Jan': 'John'}

x = input('POdaj 2 liczby do dzielenia \n').split()

try:
    result = int(x[0]) / int(x[1])
except IndexError:
    print('blad, zakladam ze result to pierwsza liczba')
    result = int(x[0])
except ZeroDivisionError:
    print('zakladamze result to 0')
    result = 1
except ValueError:
    print('zakaladam ze result to 1')
    result = 0
else:
    print(f'udalo sie - tworze plik z logami')
finally:
    print('finally - koniec')
    print(f'wynik to: {result}')