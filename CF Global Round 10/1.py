def solve(arr):
    tes = set(arr)
    # print tes

    if len(tes)==1:
        return len(arr)
    else:
        return 1

for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    print solve(arr)

