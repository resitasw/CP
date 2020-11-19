for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    kosong = []
    ans = 'NO'
    for i in arr:
        if i not in kosong:
            kosong.append(i)
        else:
            ans = 'YES'
            
    print ans
    