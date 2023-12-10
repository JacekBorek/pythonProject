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

def suggest_name(name):
    return name + '1'

users_database = {
    'Kamil': '123',
    'Jacek': '000',
    'koles21': '211'
}

