# program sprawdza tresc ile jest slow i ile dane slowa sie powtarzaja



from functions import *

content = read_file('u2.txt')
content = clear_text(content)

print(f'Liczba slow: {no_of_words(content)}')
print(f'liczba roznych slow: {no_of_unique_words(content)}')
print(f'Powtórzenia: {words_repeat(content)}')

#jeśli któreś słowo powtarza się w tekście więcej niż 5% napisz komunikat o tym