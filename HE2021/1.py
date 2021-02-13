
# // Write your code here
from collections import defaultdict
def solve(a,b):
    adict = defaultdict(int)
    bdict = defaultdict(int)
    dif = 0

    for i in a:
        adict[i] += 1
    for j in b:
        bdict[j] += 1
    nah = [z for z in adict]
    noh = [x for x in bdict]
    # print(nah + noh)
    for k in set(nah+noh):
        dif += abs(adict[k]-bdict[k])
    if dif>2:
        return "NO"
    return "YES"

for _ in range(input()):
    n = input()
    first = raw_input()
    second = raw_input()
    print solve(first,second)


