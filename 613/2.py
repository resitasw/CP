def solve(a,p,arr,parr):
    if p==a-1:
        return "YES"
    for i in range(a):
        for j in range(a-1):
            idx=j+1
            if (idx in parr) and (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    for k in xrange(a-1):
        if arr[k]>arr[k+1]:
            return "NO"
    return "YES"
                    



for _ in range(input()):
    a,p = raw_input().split()
    a = int(a)
    p=int(p)
    arr = map(int,raw_input().split())
    parr = map(int,raw_input().split())
    print solve(a,p,arr,parr)