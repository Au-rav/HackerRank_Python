a = set(map(int, input().split()))
n = int(input())
for i in range(n):
    b =set(map(int, input().split(' ')))
print(b.issubset(a) and not(a.issubset(b))