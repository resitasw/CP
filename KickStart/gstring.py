def solve(kata,k,n):
    res = 0
    idn = n//2
    for i in range(idn):
        if kata[i] != kata[-(i+1)]:
            res += 1
    return abs(res-k)

    return ans
for m in range(int(input())):
    n, k = map(int, raw_input().split())
    kata = raw_input()
    res = "Case #" + str(m+1)+": "+str(solve(kata,k,n))
    print res