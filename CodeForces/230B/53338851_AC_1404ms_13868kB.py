import sys

input = sys.stdin.readline
print = sys.stdout.write

tamanho_lista = int(input())
lista = [int(k) for k in input().split()]

def tem_tres_divisores(num):
    raiz = int(num ** 0.5)
    
    # quadrado perfeito
    if raiz * raiz != num:
        return False
    
    # raiz é primo
    if raiz <= 1:
        return False
    if raiz == 2:
        return True
    if raiz % 2 == 0:
        return False
    for i in range(3, int(raiz ** 0.5) + 1, 2):
        if raiz % i == 0:
            return False
    
    return True

for i in lista:
    if tem_tres_divisores(i):
        print("YES\n")
    else:
        print("NO\n")
