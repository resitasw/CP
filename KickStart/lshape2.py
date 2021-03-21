from collections import defaultdict

def solve(grid,r,c):
    res = 0

    segment_dict = defaultdict(lambda : [False,False])
    def cari_kanan(n,m):
        start = m
        dums = m
        while True:
            try:
                if grid[n][dums] == 1:
                    grid[n][dums]='#'
                elif grid[n][dums] == '*':
                    grid[n][dums] = 'x'
                else:
                    dums-=1
                    break
            except:
                dums -=1
                break
            dums += 1
        # print("CARI KANAN",n,m)
        for k in range(start,dums+1):
            segment_dict[(n,k)][1]=(start,dums)

        
    
    def cari_bawah(n,m):
        start = n
        dums = n
        while True:
            try:
                if grid[dums][m] == 1:
                    grid[dums][m]='*'
                elif grid[dums][m] == '#':
                    grid[dums][m] = 'x'
                else:
                    dums -= 1
                    break
            except:
                dums -=1
                break
            dums += 1
        # print("CARI BAWAH",n,m)
        for k in range(start,dums+1):
            segment_dict[(k,m)][0]=(start,dums)

        

            # grid[n][dums]
    def hitung(n,m):
        
        
        kanan_kiri = segment_dict[(n,m)][1]
        atas_bawah = segment_dict[(n,m)][0]
        kanan = kanan_kiri[1]-m + 1 
        kiri = m-kanan_kiri[0]+1 
        atas = (n - atas_bawah[0] + 1) 
        bawah = atas_bawah[1] - n +1 
        res = 0

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
        # print("hitung")
        # pprint(segment_dict[(n,m)])
        # print("KANAN KIRI ATAS BAWAH")
        # print(kanan,kiri,atas,bawah)
        # print(n,m,res)
        return res

    for i in range(r):
        for j in range(c):
            # print(i,j,grid[i][j])
            isi = grid[i][j]
            if  isi == 1:
                cari_kanan(i,j)
                cari_bawah(i,j)
            elif isi == '*':
                cari_kanan(i,j)
            elif isi == '#':
                cari_bawah(i,j)
            if grid[i][j] == 'x':
                res += hitung(i,j)
            
    
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