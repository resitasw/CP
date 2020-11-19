def solve(n,x,a,b):
    if x >= n-2:
        return n-1

    if a>b:
        b,a = a,b

    if a-1<=x:
        x = x-a+1
        a = 1
    else:
        a = a-x
        x = 0
        # return abs(a-b)
    print a
    print x
    if x>0:
        if n-b <= x:
            b = n
        else:
            b = b+x
    print b
    print x
    return b-a

for _ in range(input()):
    n, x , a, b = raw_input().split()
    n = int(n)
    x = int(x)
    a = int(a)
    b = int(b)
    print solve(n,x,a,b)