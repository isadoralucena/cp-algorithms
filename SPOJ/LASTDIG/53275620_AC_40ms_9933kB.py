n = int(input())

modulo = 10
    
def exponenciacao(a, b, modulo):
    a %= modulo
    res = 1
    while b > 0:
        if b & 1: # and em binário (checa se é ímpar)
            res = res * a % modulo
        a = a * a % modulo
        b >>= 1 # divide por 2 em binário
    return res
        
for i in range(n):
    a, b = map(int, input().split())
    print(f"{exponenciacao(a, b, modulo)}")
