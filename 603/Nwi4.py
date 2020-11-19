from sys import stdin
from string import lowercase
def main(o=ord):
    n = int(stdin.readline())
    d = {c: set() for c in lowercase}
    for w in map(set, stdin.read().split()):
        c = w.pop()
        d[c] |= w
        d[c].add(c)
    for c in lowercase:
        t = d[c].copy()
        for y in t:
            d[c] |= d[y]
        for y in d[c]:
            d[y] |= d[c]
    print len(set(frozenset(d[c]) for c in lowercase if d[c]))
main()