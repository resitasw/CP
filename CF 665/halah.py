def halah(a,b,x,y,n):
    stepa = a-x
    stepb = b-y
    anew = 0
    bnew = 0
    n_old = n

    # a duluan
    adul =0
    if stepa>n:
        anew = a-n
        bnew = b
    else:
        anew = x
        n -= stepa
        if stepb>n:
            bnew = b-n
        else:
            bnew = y
    adul = anew*bnew


    anew = 0
    bnew = 0
    bdul =0
    n=n_old
    if stepb>n:
        bnew = b-n
        anew = a
    else:
        bnew = y
        n -= stepb
        if stepa>n:
            anew = a-n
        else:
            anew = x

    bdul = anew*bnew


    if adul>bdul:
        return bdul
    else:
        return adul

for _ in range(input()):
    a,b,x,y,n = raw_input().split()
    a = int(a)
    b = int(b)
    x= int(x)
    y = int(y)
    n= int(n)
    print(halah(a,b,x,y,n))

