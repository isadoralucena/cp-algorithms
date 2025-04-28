import sys
import bisect

tamanhoArray, valorDaSoma = map(int, input().split())

array = list(map(int, input().split()))

array_sorted = sorted((valor, index + 1) for index, valor in enumerate(array))

for i in range(tamanhoArray):
    valor_atual, indice_atual = array_sorted[i]
    complemento = valorDaSoma - valor_atual
    
    index = bisect.bisect_left(array_sorted, (complemento, -1), i + 1)
    
    if index < tamanhoArray and array_sorted[index][0] == complemento and array_sorted[index][1] != indice_atual:
        
        print(f"{array_sorted[index][1]} {indice_atual} ")
        sys.exit()

print("IMPOSSIBLE")