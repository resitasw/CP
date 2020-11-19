def buang(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            arr[i] = 0


def solve(arr):
    langkah = 0
    while True:
        buang(arr)
        if not arr:
            return langkah
        m = max(arr)
        if m == 0:
            return langkah
        for i in range(len(arr)):
            if arr[i] == m:
                arr[i] = arr[i] / 2
        langkah += 1


t = int(raw_input())
for j in range(t):
    gp = input()
    arr = map(int, raw_input().split())
    print solve(arr)