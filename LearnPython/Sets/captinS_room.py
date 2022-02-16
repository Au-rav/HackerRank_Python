k = int(input())
s = input().split()
for i in s:
    if s.count(i) < k:
        print(i)