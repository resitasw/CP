def check(elem):
    bebe = 0
    for i in range(n):
        if ar[i] + bebe > elem:
            return False
        bebe += ar[i]
        if bebe == elem:
            bebe = 0
    return True
 
 
for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    x = sum(ar)
    kek = []
    i = 1
    while i <= n:
        if x % i == 0:
            kek.append(i)
        i += 1
    kek.reverse()
    ans = n - 1
    for elem in kek:
        if check(x // elem):
            ans = n - elem
            break
    print(ans)