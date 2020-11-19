def solve(arr):
    res = 0
    for i in range(len(arr)):
        if arr[i]<0:
            res -= arr[i]
        elif i!=(len(arr)-1):
            arr[i+1]+= arr[i]
    return res

for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    print solve(arr)