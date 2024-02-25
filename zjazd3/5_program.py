# dany jest spis użytkowników i haseł
# program pozwala dodać użytkowników do bazy
# program sprawdza czy nazwa użytkownika jest wolna
# jeżeli nazwa zajęta, program proponuje własną nazwę

from funkcje_5 import *

def add_user(username):
    while True:
        passwd1 = input('podaj nowe hasło: \n')
        passwd2 = input('Powtórz hasło: \n')
        if passwd1 == passwd2:
            users_database[new_user] = passwd1
            break
        else:
            print('Hasła nie pasują')

def login_succesful(username):
    passwd = input('Podaj hasło: \n')
    if passwd == users_database[username]:
        print('Hasło poprawne')
        return True
    else:
        print('Hasło niepoprawne')
        return False

def username_availabe(username):
    if username not in users_database:
        print('Nazwa użytkownika zajęta')
        return True
    else:
        print('Wprowadź nowego użytkownika')
        return False

users_database = {
    'Kamil': '123',
    'Jacek': '000',
    'koles21': '211'
}


new_user = input('Dodaj nowego użytkownika do bazy: \n')

if not username_availabe(new_user):
    print('Użytkownik rozpoznany')
    if login_succesful(new_user):
        print('Dalsza część programu')
    else:
        exit()
else:
    add_user(new_user)
print(users_database)