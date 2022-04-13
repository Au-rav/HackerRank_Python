from collections import deque


for i in range(int(input())):
    n, blocks = input(), deque(map(int, input().split()))
    ans = True

    for j in range(len(blocks) - 1):
        if blocks[0] >= blocks[1]:
            blocks.popleft()
        elif blocks[-1] >= blocks[-2]:
            blocks.pop()
        else:
            ans = False
            break

    print('Yes' if ans else 'No')