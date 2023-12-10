lista = []

listaliczb = [1, 2, 2.5, 3, 4, 1.5]
listamieszana = ["mama", 0, True, -5, "kajak"]
listastringow = ["kajak", "mama", "oko", "maroko"]

print(listaliczb[3]);

print(listamieszana[-1]);

print(listamieszana[-1][0]);

print("dodawanie do listy")
lista = ["tata"]
print(lista)

lista.append("mama")
print(lista)
lista = lista + ["syn"]
print(lista)
lista.extend(["ciotka"])
print(lista)
#przy dodawaniu więcej niż 1 pozycji wykorzystujemy funkcję extend

lista.insert(2, "babcia")
print(lista)

print(listaliczb)
listaliczb.sort(reverse=True)
print(listaliczb)

print(listaliczb.count(1))

print(lista.pop())
#ostatnia pozycja z listy
#funkcja pop usuwa z listy ale nadal mamy ten element

print(listaliczb.remove(3))
print(listaliczb)

print(listaliczb.clear())
print(listaliczb)
#lista jest mutowalna
#usuwanie elementu na stałe
del lista[-1]
print(lista)