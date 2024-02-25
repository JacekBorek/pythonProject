#napisac program ktory pozwoli uzytkownikowi
#1: dodawac nowe definicje
#2: szukac istniejacych definicji
#3: usuwac wybrane definicje

#utworzenie pustego słownika
definicje = {}

while True:
    print("1: Dodaj definicję")
    print("2: Szukaj definicję")
    print("3: Usuń definicję")
    print("4: Wyświetl wszystkiego definicje")
    print("5: Zakończ")

    wybor = input("Co chcesz zrobić?: ")

    if wybor == "1":
        klucz = input("Podaj słowo kluczowe: ")
        definicja = input("Podaj definicję: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie")
    elif wybor == "2":
        klucz = input("Jakiego słowa szukasz? ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Brak definicji w słowniku!")
    elif wybor == "3":
        klucz = input("Podaj słowo do usunięcia: ")
        if klucz in definicje:
            del definicje[klucz]
            print("Definicja", klucz, "została usunięta") #Spróbuj dodać nazwę definicji
        else:
            print("Brak definicji w słowniku!")
    elif wybor == "4": #w domu wyświetl wszystkie definicje
        pass
    elif wybor == "5":
        break


