def solve(a,k):
    if a<k:
        hasil = k-a
        return hasil
    else:
        if (a-k)%2==0:
            return 0
        else:
            return 1
            
for _ in range(input()):
    a,k = raw_input().split()
    k = int(k)
    a = int(a)
    
    print solve(a,k)