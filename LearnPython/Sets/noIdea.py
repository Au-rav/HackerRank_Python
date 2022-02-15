n1,n2 = input().split()
arr1 =  input().split()
a = set(input().split())
b = set(input().split())
happy =  0
for i in arr1:
    if i in a:
        happy+=1
    elif i in b:
        happy-=1
print(happy)