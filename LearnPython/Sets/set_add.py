n = int(input()) 
stamps = []
sample_set = set()
for i in range(n):
    l = input()
    stamps.append(l)
#print(stamps)
for elem in stamps:
    # add each element to the set
    sample_set.add(elem)
print(len(sample_set))