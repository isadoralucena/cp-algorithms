n, k = map(int, input().split())
a = [int(n) for n in input().split()]

a.sort()

smaller = float('inf')

for i in range(k + 1):
    smaller = min(a[i + (n - k) -1] - a[i], smaller)
print(smaller)