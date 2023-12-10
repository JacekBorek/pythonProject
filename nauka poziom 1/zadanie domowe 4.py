a = [2, 52, 5, 7, 12, 67, 22, 31]

for i in range(0, len(a)-1, 2):
    a[i], a[i+1]=a[i+1], a[i]

print(a)