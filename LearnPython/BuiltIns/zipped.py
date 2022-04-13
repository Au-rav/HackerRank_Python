N,X = map(int,input().split())
grades = []

for i in range(X):
    grades.append(map(float,input().split()))               
for i in zip(*grades):
    print(sum(i)/len(i))