
def solve(n,arr):
    arr.sort()
    res = True
    if arr[0]+arr[1]>n:
        for i in arr:
            if i >n:
                return "NO"
        return "YES"
    else:
        return "YES"


    
    


for _ in range(input()):
    m,n = map(int,raw_input().split())
    arr = map(int,raw_input().split())
    
    print solve(n,arr)
    