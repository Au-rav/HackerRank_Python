# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

result =[]
for x in range(0,T):
    string = input()
    evenChar = []
    oddChar = []    
    for index in range(len(string)):
        if not (index%2):
            evenChar.append(string[index])
        else: 
            oddChar.append(string[index])
    result.append(''.join(evenChar)+" "+''.join(oddChar))  

[print(_) for _ in result]
