from collections import defaultdict
def solve(arr):
    res = defaultdict(int)
    res_2 = []
    for i in arr:
        res[i]+=1
    for y in res:
        if res[y] == 1:
            res_2.append(y)
    if res_2:
        return arr.index(min(res_2))+1
    
    return -1
    


for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    print solve(arr)
    