def mnozenie(x, y):
    result = round(x * y)
    return result

print(mnozenie(23, 23) + 100)

def dzielenie(x, y):
    if y == 0:
        print(f'Dzielenie przez 0, zwracam wartość 1')
        return 1
    else:
        return x / y

print(dzielenie(2,5))
