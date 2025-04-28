n = int(input())

for i in range(n):
    n1, n2, n3  = [int(n) for n in input().split()]
    if n1 < n2 < n3:
        print("STAIR")
    elif n1 < n2 > n3:
        print("PEAK")
    else:
        print("NONE")