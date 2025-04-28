num_caixas = int(input())
caixas = [int(n) for n in input().split()]
    
caixas.sort()

i = 0
while True:
    if i >= len(caixas): break
    for j in range(i - 1, -1, -1):
        if caixas[i] > caixas[j]:
            caixas.pop(j)
            i -= 1
            break
    i += 1


print(len(caixas))