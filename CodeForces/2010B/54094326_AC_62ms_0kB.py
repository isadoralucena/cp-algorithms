n1, n2 = [int(n) for n in input().split()]

if (n1 == 1 and n2 == 2) or (n1 == 2 and n2 == 1):
    print(3)
elif (n1 == 1 and n2 == 3) or (n1 == 3 and n2 == 1):
    print(2)
elif (n1 == 2 and n2 == 3) or (n1 == 3 and n2 == 2):
    print(1)