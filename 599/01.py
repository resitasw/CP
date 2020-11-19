def solve(arr):
    arr = arr.sort()

    for i in range(len(arr)):
        if arr[i]<= len(arr)-i:
            hasil = i+1
    return hasil

for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    print solve(arr)

