from math import ceil
def solve(n,k):
    if n<=k:
        return ceil(k/n)
    elif n%k:
        return 2
    else:
        return 1


    
    


for _ in range(int(input())):
    n,k = map(int,input().split())
    
    print(solve(n,k))
    