def solve(n):
    strnum = str(n)
    panjang = len(strnum)
    if panjang==1:
        return n
    hasil = (panjang-1)*9
    ons = strnum[0]*panjang
    onsnum = int(ons)

    if onsnum > n:

        hasil += int(strnum[0])-1
        print hasil
    else:
        hasil += int(strnum[0])

    return hasil


t = int(raw_input())
for _ in range(t):
    n = input()
    print solve(n)