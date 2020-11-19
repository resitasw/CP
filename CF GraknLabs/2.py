def solve(n,k,arr):
    arr_set = len(set(arr))
    if arr_set<=k:
        return 1
    if k==1:
        return -1
    
    res =[arr]
    inde = 0
    while True:
        counter = 0
        second = []
        last = -1
        for i in range(n):
            if res[inde][i]!=last and counter<k:
                counter +=1
                last = res[inde][i]
            
            second.append(res[inde][i]-last)
            res[inde][i] = last
        if len(set(second))==1:
            break
        res.append(second)
        inde +=1
    
    return len(res)
    


    
    hm = len(set(second))
    if hm<=k:
        return 2
    else:
        return -1
for _ in range(input()):
    n,k = map(int,raw_input().split())
    arr = map(int,raw_input().split())

    print solve(n,k,arr)