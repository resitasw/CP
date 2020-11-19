def solve(n,arr):
    y = min(arr)
    indexes = []
    isi = []
    for i in range(n):
        if arr[i]%y == 0:
            indexes.append(i)
            isi.append(arr[i])
    isi.sort()
    for j in range(len(indexes)):
        arr[indexes[j]]=isi[j]
    for k in range(n-1):
        if arr[k]>arr[k+1]:
            return "NO"
    return "YES"
for _ in range(input()):
    n = input()
    n = int(n)
    arr = map(int,raw_input().split())
    print solve(n,arr)