
def solve(n):
    ans=0
    for i in range(101):
        if n//(10**i):
            ans+=1
        else:
            break
    return ans


    
    


for _ in range(input()):
    n = input()
    
    print solve(n)
    