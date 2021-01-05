def solve(arr):
    satuan = 0
    tot = 0
    for i in arr:
        tot += i
        if i == 1:
            satuan+=1
    
    if tot%2==0:
        hehe = tot/2
        if hehe%2:
            if satuan:
                return "YES"
            else:
                return "NO"
        else:
            return "YES"
    else:
        return "NO"


for _ in range(input()):
    hm = raw_input()
    arr = map(int,raw_input().split())
    
    print solve(arr)