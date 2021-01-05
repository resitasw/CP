def solve(w,h,n):
    a = 0
    b = 0
    while (not w%2):
        a+=1
        w /=2
    while (not h%2):
        a+=1
        h/=2
    res = 2**a
    if res>=n:
        return "YES"
    return "NO"

for _ in range(input()):
    # hm = raw_input()
    w,h,n = map(int,raw_input().split())
    
    print solve(w,h,n)