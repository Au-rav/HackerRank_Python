# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
num_of_sets = int(input())

for i in range(num_of_sets):
    command = input().split()
    if command[0] == 'intersection_update':
        int_up = set(map(int, input().split()))
        s.intersection_update(int_up)
    if command[0]=="update":
        up = set(map(int, input().split()))
        s.update(up)
    if command[0]=="symmetric_difference_update":
        sym_diff = set(map(int, input().split()))
        s.symmetric_difference_update(sym_diff)
    if command[0]=="difference_update":
        diff_up = set(map(int, input().split()))
        s.difference_update(diff_up)
print(sum(s))