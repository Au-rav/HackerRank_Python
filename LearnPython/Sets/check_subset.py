# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))
    