t = int(input())

while t:
    t-=1
    n, k = map(int, input().split())
    if k >= n-1:
        print(1)
    else:
        print(n)
    