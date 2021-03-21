from pprint import pprint
def cari(grid,r,c):
    res = 0
    kanan = 1
    kiri = 1
    atas = 1
    bawah = 1
    # kanan
    for i in range(c+1,len(grid[r])):
        if not grid[r][i]:
            break
        kanan += 1
    
    # kiri
    for i in range(c-1,-1,-1):
        if not grid[r][i]:
            break
        kiri += 1
    
    # atas 
    for i in range(r-1,-1,-1):
        if not grid[i][c]:
            break
        atas += 1

    # bawah 
    for i in range(r+1,len(grid)):
        if not grid[i][c]:
            break
        bawah += 1
    
    
    if kanan>1:
        # atas kanan
        if atas>1:
            # panjang atas
            res += min(atas/2 -1,kanan-1)
            res += min(kanan/2 -1, atas-1)
        if bawah > 1:
            res += min(bawah/2 -1,kanan-1)
            res += min(kanan/2 -1, bawah-1)
    
    #kiri atas
    if kiri>1:
        if atas>1:
            # panjang atas
            res += min(atas/2 -1,kiri-1)
            res += min(kiri/2 -1, atas-1)
        if bawah > 1:
            res += min(bawah/2 -1,kiri-1)
            res += min(kiri/2 -1, bawah-1)
        
    return res

def solve(grid,r,c):
    res = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j]:
                try:
                    row_kanan = grid[i][j+1] != 0
                except:
                    row_kanan = False
                if j-1>=0:
                    row_kiri = grid[i][j-1] !=0
                else:
                    row_kiri = False
                is_r_seg = row_kanan or row_kiri

                if i-1>=0:
                    col_atas = grid[i-1][j] != 0
                else:
                    col_atas = False
                try:
                    col_bawah = grid[i+1][j] !=0
                except:
                    col_bawah = False
                is_c_seg = col_atas or col_bawah
                # if i==1 and j==0:
                    # print is_c_seg,is_r_seg
                if is_c_seg and is_r_seg:
                    res += cari(grid,i,j)
    return res


    return grid
for m in range(int(input())):
    r, c = map(int, raw_input().split())
    grid = []
    for i in range(r):
        col = map(int, raw_input().split())
        grid.append(col)
    # pprint(grid)
    res = "Case #" + str(m+1)+": "+str(solve(grid,r,c))
    print res
    # pprint(solve(grid,r,c))