from collections import defaultdict

def hitung(mak,anak):
    m = len(mak)
    a = len(anak)
    res = 0
    # print(m-a)
    for i in range(m-a+1):
        if i !=m-a+1:
            if anak == mak[i:i+a]:
                res += 1
            else:
                continue
        else:
            if anak == mak[i:]:
                res+=1
    return res



search_dict = defaultdict(lambda: None)
n, q = map(int,raw_input().split())
s = raw_input()
lama_oke = True
for i in range(q):
    semua = raw_input().split()
    if semua[0] == '1':
        # print("type 1")
        # print(semua)
        if search_dict[semua[1]] is not None:
            # print("langsong")
            print(search_dict[semua[1]])
        else: 
            # print("cari dolo")
            ini = hitung(s,semua[1])
            print(ini)
            search_dict[semua[1]]=ini
    elif semua[0]=='2':
        search_dict = defaultdict(lambda: None)
        # print("type 2")
        # print(semua)
        l,r = map(int,semua[1:3])
        hm = semua[3]
        if r!= len(s):
            depan = s[:l-1]
            belakang = s[r:]
            s = depan +hm + belakang
        else:
            depan = s[:l-1]
            # belakang = s[r:]
            s = depan +hm

# print(hitung("aaaa","aa"))
        udysghjsgjhagj
