def solve(a,b,c):
    res =[]
    for i in range(len(a)):
        if i==0:
            res.append(a[i])
            continue
        if i==(len(a)-1):
            n = len(a)
            if a[i] not in [res[n-2],res[0]]:
                res.append(a[i])
            elif b[i] not in [res[n-2],res[0]]:
                res.append(b[i])
            else:
                res.append(c[i])
            continue


        if a[i] != res[i-1]:
            res.append(a[i])
        else:
            res.append(b[i])
    
    hasil = ' '.join(map(str,res))
    return hasil


for _ in range(input()):
    n = input()
    arra = map(int,raw_input().split())
    arrb = map(int,raw_input().split())
    arrc = map(int,raw_input().split())

    print solve(arra,arrb,arrc)