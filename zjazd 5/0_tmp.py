print('string split')
my_string = 'Mama.kupila.psa'
splitted_string = my_string.split('.')
print(f'string przed podzialem: {my_string}')
print(f'string po podziale (dzielimy po kopce): {splitted_string}')

print('\nusuwanie znaków')
my_string = 'Mama.kupila.psa'
my_string = my_string.replace('.','')
print(f'string po usunięciu kropki: {my_string}')

print('\nFunkcje')
def after_a(text):
    return text[text.index('a')+1]

my_string = 'Mama.kupila.psa'
print(after_a(my_string))

print('\nZbiory')
zbior1 = {'.', ',', '(', '\'', '\"'}
zbior2 = set('.,(\'\"')
print(f'zbior1: {zbior1}')
print(f'zbior2: {zbior2}')

def draw_lines(x, y, *coordinates):
    start = [x, y]
    for i in range(0, len(coordinates), 2):
        print(f'rysuje linie z {start} do {coordinates}')
        start = [coordinates[i], coordinates[i+1]]

draw_lines(2, 2, 1, 1, 3, 4)

def triangle(**data):
    if 'a' in data.keys() and 'b' in data.keys() and 'c' in data.keys():
        print(f'Licze pole trojkata z 3 bokow')
    elif 'a' in data.keys() and 'b' in data.keys() and 'alpha' in data.keys():
        print(f'licze pole trojkata z 2 bokow i kata')
    elif 'a' in data.keys() and 'alpha' in data.keys() and 'beta' in data.keys():
        print(f'licze pole trojkata z boku i 2 katow')
    elif 'a' in data.keys() and 'h' in data.keys():
        print(f'licze pole trojka z boku i wysokosci')
    else:
        print(f'nie da sie policzyc pola')

triangle(a=5, alpha=22, beta=22)


login_database = ['Jaco', 'Stachu999', 'Paulina94', 'Wiolczi18']

def check_logins(*logins):
    available_login_list = []
    for login in logins:
        if login not in login_database:
            print(f'Login {login} jest dostepny')
            available_login_list.append(login)
    return available_login_list

print(check_logins('Jaco', 'Stachu999', 'Paulina94', 'Wiolczi18'))

def final_function(b, a=1, c=0):
    return a + b + c

print(final_function(4,5))

def final2(a, b, *rest, c=1, **kwargs):
    