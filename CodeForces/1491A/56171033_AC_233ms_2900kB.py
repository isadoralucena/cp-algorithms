comprimento_matriz, numero_consultas = map(int, input().split())

matriz = [int(comprimento_matriz) for comprimento_matriz in input().split()]
numero0 = matriz.count(0)
numero1 = matriz.count(1)

result=""
for i in range(numero_consultas):
    opcao, valor = map(int, input().split())
    if(opcao==1):
        if(matriz[valor-1] == 0):
            matriz[valor-1] = 1
            numero0 = numero0 - 1
            numero1 = numero1 + 1
        else:
            matriz[valor-1] = 0
            numero0 = numero0 + 1
            numero1 = numero1 - 1
    else:
        if(numero1 >= valor):
            result += f"1\n"
        else:
            result += f"0\n"

print(result)
