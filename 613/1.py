def solve(a,b):
    selisih = a-b
    if selisih == 0:
        return 0
    if selisih>0:
        if selisih%2==0:
            return 1
        else:
            return 2
    else:
        if selisih%2==1:
            return 1
        else:
            return 2
    
for _ in range(input()):
    a,b = raw_input().split()
    a = int(a)
    b=int(b)
    print solve(a,b)

    