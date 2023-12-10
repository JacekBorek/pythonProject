def welcome(name, age):
    if age <= 20:
        print(f'Cześć {name}')
    else:
        if name[-1] == "a" or name[-1] == 'e':
            print(f'Szanowna pani {name}')
        else:
            print(f'Szanowny Panie {name}')


username = input('Podaj swoje imię: \n')
age = int(input('Podaj swój wiek: \n'))


welcome(username, age)

welcome('Jacek', 31)

# import random
# lista_imion = ['Jacek', 'Basia', 'Paulina', 'Tomek']
# welcome(lista_imion[1], random.randint(3, 52))
#     if gender.lower == 'k':
#         print('Szanowna Pani ',username)
#     else:
#         print("Szanowny Panie ",username)