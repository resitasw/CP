def solve(arr):
    ini = {}
    itu = []
    for m in arr:
        ini[m]=1
    for angka in ini:
        itu.append(angka)
    mina = min(itu)
    maxa = max(itu)
    if maxa-mina+1>len(itu):
        return("NO")
    return("YES")

for _ in range(input()):
    n = raw_input()
    arr = map(int,raw_input().split())
    # parr = map(int,raw_input().split())
    print solve(arr)