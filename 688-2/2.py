def mana(selisih):

    nilai_antara = []
    for i in range(len(selisih)-1):
        nilai_antara.append(selisih[i]+selisih[i+1])
    selisih2 = map(abs,selisih)
    nyoh = sum(selisih2[1:])
    dum = sum(selisih2[:len(selisih)-1])
    hah = sum(selisih2)
    if dum<nyoh:
        nyoh = dum
    for k in range(len(selisih)-1):
        # dum = abs(nilai_antara[k])
        # if k ==0:
        #     dum += sum(selisih2[2:])
        # else:
        dum = hah -(selisih2[k])-(selisih2[k+1]) + abs(nilai_antara[k])
            # dum -= (selisih2[k+1])
        if dum<nyoh:
            nyoh = dum
    return nyoh

        
        
    
def solve(a):
    if len(a)==1:
        return 0
    if len(a)==2:
        return abs(a[0]-a[1])
    selisih = []
    for i in range(len(a)-1):
        selisih.append(a[i]-a[i+1])
    # print("selisih",selisih)
    
    hasil = float('inf')
    if len(selisih)==2:
        for j in selisih:
            if abs(j)<hasil:
                hasil = abs(j)
        return hasil
    return mana(selisih)


for _ in range(input()):
    n = map(int,raw_input().split())
    a = map(int,raw_input().split())
    
    
    print solve(a)
    