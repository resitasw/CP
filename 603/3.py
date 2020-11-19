from __future__ import division


def solve(n):
    new = n
    start = 1
    old = 0
    hasil =[]
    while(new>0):
        new = n//start
        if new != old:
            hasil.insert(0,new)
        old = new
        start +=1

    print len(hasil)
    streng =""
    for i in range(len(hasil)):
        streng = streng + str(hasil[i])+" "
    print streng



for _ in range(input()):
    n = input()
    solve(n)