def solve(arr):
    arr.reverse()
    arr = map(str,arr)
    arr1 = ' '.join(arr)
    return arr1

for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    print solve(arr)