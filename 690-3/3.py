def solve(arr):
    awal = arr
    digs = ''
    for i in range(9,0,-1):
        if awal-i<=0:
            digs = str(awal) + digs
            awal -= awal
            break
        else:
            digs = str(i) + digs
            awal -= i
    if awal:
        return -1
    return digs
        


for _ in range(input()):
    hm = input()
    
    
    print solve(hm)