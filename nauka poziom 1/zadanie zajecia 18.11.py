#program ktory wyswietli menu dla uzytkownika
#uzytkownik ma do wyboru kilka opcji: dodaj zadaanie, wyswietl zadanie, usun zadanie, zakoncz program
#po wybraniu danej opcji , program wykonuje dana czynnosc

todo = []
while True:
    print("~~~~~~Menu~~~~~~")
    print("1: dodaj zadanie")
    print("2: wyswietl zadanie")
    print("3: usun zadanie")
    print("4: zakoncz program")

    wybor = input("wybierz opcje z menu: ")

    if wybor == 1:
        zadanie = input("podaj nazwe zadania: ")
        todo.append(zadanie)
        print("zadanie dodane")

    if wybor == "1":
        zadanie = input("Podaj nazwę zadania: ")
        todo.append(zadanie)
        print("Zadanie dodane")
    elif wybor == "2":
        # wyświetl zadania >> ładnie wyświetl zadania (w formie listy, jedno zadnie pod drugim)
        print("Twoje zadania to:", todo)
    elif wybor == "3":
        # usuń zadanie
        co_usunac = int(input("Podaj index zadania do usuniecia "))
        del todo[co_usunac - 1]
        # zad dom. przed usuwaniem lepiej wyswietlic cala liste zadań
    elif wybor == "4":
        # wyświetl zadania
        break
    else:
        print("Nie rozumiem komendy")