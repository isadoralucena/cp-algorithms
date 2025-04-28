n = int(input())
precos = sorted([int(n) for n in input().split()])
q = int(input())
moedas = []
for i in range(q):
    moedas.append(int(input()))


def busca_binaria(valor, lista):
    l = 0
    r = len(lista)-1
    indice = -1
    while l <= r:
        mid = (l+r)//2
        if lista[mid] <= valor:
            indice = mid
            l = mid + 1
        else:
            r = mid -1
            
    return indice

minim = min(precos)
for i in range(q):
    indice = busca_binaria(moedas[i], precos)
    print(indice+1)