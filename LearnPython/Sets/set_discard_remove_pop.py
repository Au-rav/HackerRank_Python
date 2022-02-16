n = int(input())
s = set(map(int, input().split()))
num_of_cmds = int(input())

for i in range(num_of_cmds):
    command = input().split()
    if command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0]=="discard":
        s.discard(int(command[1]))
    else :
        s.pop()
print(sum(s))