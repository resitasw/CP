def solve(n,m,s,kesalahan):
    per_index = [1 for i in xrange(n)]
    hrf = []
    hasil=''
    kes = [0 for i in range(n)]
    for i in xrange(m):
        kes[kesalahan[i]-1]+=1
    total = sum(kes)
    for i in xrange(n):
        per_index[i]+=total
        total-=kes[i]

    # for index in range(n):
    #     ans[s[index]] += number_sum
    #     number_sum -= number[index]
    # for l in xrange(26):
    #     hrf.append(0)
    # for i in range(n):
        # per_index.append(1)
    # for j in xrange(m):
    #     for k in xrange(kesalahan[j]):
    #         per_index[k]+=1
    # for h in xrange(n):
    #     an_iterator = filter(lambda number: number >= h, )
    for p in xrange(n):
        idx = ord(s[p])-97
        hrf[idx]+=per_index[p]
    for q in xrange(26):
        hasil = hasil + str(hrf[q])+" "
    return hasil
    

for _ in range(input()):
    n,m = raw_input().split()
    n = int(n)
    m=int(m)
    s = raw_input()
    kesalahan = map(int,raw_input().split())
    print solve(n,m,s,kesalahan)