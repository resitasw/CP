def solve(a,b):
    mina = min(a)
    minb = min(b)
    nyoh = 0
    for i in range(len(b)):
        jara = a[i]-mina
        jarb = b[i]-minb
        nyoh += max(jara,jarb)
    return nyoh

for _ in range(input()):
    n = raw_input()
    candy = map(int,raw_input().split())
    orange = map(int,raw_input().split())
    # parr = map(int,raw_input().split())
    print solve(candy,orange)