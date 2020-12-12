def solve(n,k):
    anu = n//3
    sisa = n%3
    ans = 'abc'*anu
    if sisa ==1:
        ans+='a'
    elif sisa==2:
        ans+='ab'
    return ans


for _ in range(input()):
    n,k = map(int,raw_input().split())
    
    print solve(n,k)
    