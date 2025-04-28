t = int(input())

while t > 0:
    t-=1
    input()
    a = [int(n) for n in input().split()]
    
    quant_pares = 0
    quant_imp = 0
    for num in a:
        if (num % 2 == 0):
            quant_pares +=1
        else:
            quant_imp += 1
    
    # print(quant_pares)
    # print(quant_imp)
    if(quant_pares > 0):
        print(quant_imp+1)
    elif(quant_imp > 0):
        print(quant_imp-1)
            