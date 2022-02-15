if __name__ == '__main__':
    n1 = int(input())
    arr1 = set(map(int, input().split()))
    n2 = int(input())
    arr2 = set(map(int, input().split()))
    result1 = list((arr1.union(arr2))-(arr1.intersection(arr2)))
    print(*sorted(result1),sep='\n')