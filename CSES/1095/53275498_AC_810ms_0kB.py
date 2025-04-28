n = int(input())

modulo = 1000000007
# def exponenciacao(numero, potencia):
#     if potencia == 0: return 1
#     if potencia % 2 == 0: return exponenciacao((numero%modulo) * (numero%modulo), potencia/2)
#     else: return (numero%modulo) * exponenciacao((numero%modulo), potencia - 1)
    
def exponenciacao(a, b, modulo):
    a %= modulo
    res = 1
    while b > 0:
        if b & 1: # and em binário
            res = res * a % modulo
        a = a * a % modulo
        b >>= 1 # divide por 2 em binário
    return res
        
for i in range(n):
    a, b = map(int, input().split())
    print(f"{exponenciacao(a, b, modulo)}")