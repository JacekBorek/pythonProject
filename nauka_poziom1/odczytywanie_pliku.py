with open('my_file.txt', 'r') as file1:
    # content = file1.read()
    # print(content)
    content = file1.read()
print(content)

#policz liczbę słów
print("typ zmiennej przed uzyciem split:", type(content))

content = content.lower().split()
print("typ zmiennej po uzyciu split:", type(content))
print(content)

print("liczba slow w pliku to:", len(set(content)))