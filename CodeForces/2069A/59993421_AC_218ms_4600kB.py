
t = int(input())

while t:
    t-=1
    n = int(input())
    b = str(input())
    b = b.replace(" ", "")
    if '101' in b:
        print("NO")
    else:
        print("YES")    