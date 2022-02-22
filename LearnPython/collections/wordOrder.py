from collections import *

words = []
for i in range(int(input())):
    words.append(input())
occur = Counter(words)
print(len(occur))
print(*occur.values())
