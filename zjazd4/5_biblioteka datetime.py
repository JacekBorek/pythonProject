import datetime

now = datetime.datetime.now()

print(now)

date1 = now.strftime('Dzisiaj jest %d/%m/%Y. Godzina %H:%M')

print(date1)
# now = str(now)
# hour = now[11:16]
# print(hour)