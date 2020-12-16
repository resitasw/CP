def solve(n,arr):
    if n==4:
        if arr=='2020':
            return 'YES'
        else:
            return 'NO'
    elif arr[:4]=='2020':
        return 'YES'
    elif arr[0]=='2' and arr[-3:]=='020':
        return 'YES'
    elif arr[0:2]=='20' and arr[-2:]=='20':
        return 'YES'
    elif arr[0:3]=='202' and arr[-1]=='0':
        return 'YES'
    elif arr[-4:]=='2020':
        return 'YES'
    else:
        return 'NO'


for _ in range(input()):
    hm = input()
    nih = raw_input()
    
    print solve(hm,nih)