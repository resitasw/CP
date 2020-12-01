
def solve(n):
    ans=0
    for i in range(101):
        if n//(10**i):
            ans+=1
        else:
            break
    return ans


    
    


for _ in range(input()):
    a,b = map(int,raw_input().split())
    a -=1
    print str(a)+" "+str(b) 
    