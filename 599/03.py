from __future__ import division
def faktor(n):
    hasil = []
    for i in range(1,n):
        print i
        if n%(i+1)==0:
            hasil.append(i+1)
            break
    return hasil

def solve(n):
    faktors = faktor(n)

    while n>1:
        print n
        if n//faktors[0] == n/faktors[0]:
            n /= faktors[0]
        else:
            return 1

    if n == 1:
        return faktors[0]
    else:
        return 1

n = input()
print solve(n)