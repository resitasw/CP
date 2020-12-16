def get_factor(dum,n):
    nih = []
    for i in range(n,0,-1):
        if not dum%i:
            nih.append(i)
    return nih

def ini_bisa(slice,arr):
    # pointer =0\
    sementara = 0
    for i in range(len(arr)):
        sementara += arr[i]
        if sementara > slice:
            return False
        if sementara == slice:
            sementara = 0
            
            # continue
        
    return True
        

def solve(n,arr):
    a = max(arr)
    # b = min(arr)
    if len(set(arr))==1:
        return 0
    first = {}
    dum = 0
    for i in arr:
        dum += i
    factors = get_factor(dum,n)
    if len(factors)==1:
        return n-1
    
    for j in factors:
        per_slice = dum/j
        if per_slice<a:
            continue
        if ini_bisa(per_slice,arr):
            return n - j
    return n-1


    
    
        
for _ in range(input()):
    hm = input()
    nih = map(int,raw_input().split())
    
    print solve(hm,nih)