def solve(arr):
    res = []
    for i in range(len(arr)):
        if not i%2:
            idn = i/2
        else:
            idn = 0-((i+1)/2)
        res.append(str(arr[idn]))
    res = ' '.join(res)
    return res


for _ in range(input()):
    hm = raw_input()
    nih = map(int,raw_input().split())
    
    print solve(nih)