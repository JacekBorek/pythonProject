# podejście 1
print(11 // 3)
print(11 % 3)

print('ile pomidórów chcesz kupić')
no_of_tomatos = int(input())
print('chcesz kupic')
print(no_of_tomatos)
print('pomidorow')

no_of_3packs = no_of_tomatos // 3
print('liczba 3paków')
print(no_of_3packs)

no_of_tomatos_apart = int(no_of_tomatos) - no_of_3packs * 3

print('liczba pomidorów osobno')
print(no_of_tomatos_apart)


money_to_pay = (no_of_3packs * (3 * 3 * 0,8) + no_of_tomatos_apart * 3)

print('zapłacisz')
print(money_to_pay)

