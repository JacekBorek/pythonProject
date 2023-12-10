def my_arg_function(*args):
    print(args[2])
    for arg in args:
        if arg > 0:
            print(f'{arg} * 2 to {arg * 2}')
        else:
            print(f'{arg} mniejsze od zera')

my_arg_function(3, 4, 5, -1, 2)
my_arg_function(1, 2)

def my_kwargs_function(**kwargs):
    if 'nazwisko' in kwargs and kwargs['nazwisko'] == 'Kowalski':
        print(f'Jesteś zablokowany')

my_kwargs_function(imie='Jacek', status='zonaty')