t = int(raw_input())
for _ in xrange(t):
    n = int(raw_input())
    s = [raw_input().strip() for _ in xrange(n)]
    d = {w: 0 for w in s}
    print n - len(d)
    for w in s:
        if d[w]:
            for c in '0123456789':
                nw = c + w[1:]
                if nw not in d:
                    d[nw] = 1
                    print nw
                    break
        else:
            print w
            d[w] += 1