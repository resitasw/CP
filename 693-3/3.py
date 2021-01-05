def solve(arr):
    gede = -float('inf')
    n = len(arr)
    anu = [0]*n
    for i in range(n-1,-1,-1):
        
        tot = 0
        tot+=arr[i]
        j = i+arr[i]
        if j<=n-1:
            tot += anu[j]
        anu[i]=tot
    ehe = max(anu)
    return ehe

    
    


for _ in range(input()):
    hm = raw_input()
    arr = map(int,raw_input().split())
    
    print solve(arr)