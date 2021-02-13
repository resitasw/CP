from math import ceil
def solve(n,k,arr):
    jum = 0
    res = 0
    for i in range(n):
        # print(i)
        if not i:
            jum += arr[i]
            continue
        else:
            per = (arr[i]*100)/jum
            # print(jum,per)
            if per>k:
                x = ceil(((arr[i]*100)/k)-jum)
                jum += x
                res += x
        jum += arr[i]
    return res



    
    


for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    
    print(solve(n,k,arr))
    