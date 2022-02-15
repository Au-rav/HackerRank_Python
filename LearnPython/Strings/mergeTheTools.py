def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        string_div = string[i:i+k]
        no_repeats = ' '
        for i in string_div:
            if i not in no_repeats:
                print(i, end='')
                no_repeats+=i
        print() 
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)