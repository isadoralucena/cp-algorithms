a, b = map(int, input().split())

aux = 0

for i in range(a, b + 1):
    if str(i) == str(i)[::-1]:
        aux += 1

print(aux)