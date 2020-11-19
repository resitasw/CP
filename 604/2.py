def solve(panjang,arr):
    kamus = {}
    asli = []

    for i in xrange(panjang):
        dummy = kamus.update({i+1:0})
        asli.append(i+1)

    for number in xrange(1,panjang+1):
        if number ==1:
            kamus[1]=1
            continue
        for ind in xrange(panjang-number+1):
            if ind+number>=panjang:
                dict_as = set(arr[ind:])
            else:
                dict_as = set(arr[ind:ind+number])
            if dict_as == set(asli[:number]):
                kamus[number] = 1
    for i in xrange(panjang):
        arr[i] = kamus[arr[i]]

    return ' '.join(arr)


t = int(raw_input())
for _ in xrange(t):
    panjang = int(raw_input())
    arr = map(int,raw_input().split())
    print solve(panjang,arr)
