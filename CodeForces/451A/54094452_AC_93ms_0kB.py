n, m = map(int, input().split())
menor=0
if(n==m):
    if(n%2==0):
        print("Malvika")
    else:
        print("Akshat")
else:
    if(n>m):
        menor = m
    else:
        menor = n
    if(menor%2 == 0):
        print("Malvika")
    else:
        print("Akshat")