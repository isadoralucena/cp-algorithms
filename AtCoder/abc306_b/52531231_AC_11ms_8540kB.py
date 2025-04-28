array = list(map(int, input().split()))
aux = 0
for i in range(len(array)):
    aux = aux + (array[i] * (2**i))

print(aux)