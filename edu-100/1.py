def solve(arr):
    ehe = sum(arr)
    if not ehe%9:
        ini = ehe/9
        for i in arr:
            if i<ini:
                return 'NO'
        return 'YES'
        
    else:
        return 'NO'


for _ in range(input()):
    # hm = raw_input()
    nih = map(int,raw_input().split())
    
    print solve(nih)