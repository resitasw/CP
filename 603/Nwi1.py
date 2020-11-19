t = int(raw_input())
for _ in xrange(t):
    a = map(int, raw_input().split())
    a.sort()
    if a[0] + a[1] < a[2]:
        print a[0] + a[1]
    else:
        print sum(a) / 2