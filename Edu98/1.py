def solve(x,y):
    ans= 0
    if abs(x-y)<=1:
        return x+y
    if x>y:
        ans += (y*2+1)
        x = x-y-1
        ans += (x*2)
    else:
        ans += (x*2+1)
        y = y-x-1
        ans += (y*2)
    return ans


for _ in range(input()):
    x,y = raw_input().split()
    x = int(x)
    y = int(y)
    
    print solve(x,y)