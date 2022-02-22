from collections import Counter
x = int(input())
shoesize = Counter(map(int, input().split()))
n = int(input())
total = 0
for i in range(n):
    cust_size, price = map(int, input().split())
    if cust_size in shoesize and shoesize[cust_size]!=0:
        total  = total + price
        shoesize[cust_size] -= 1
print(total)