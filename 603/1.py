from __future__ import division


def solve(n):
    arr = [a, b, c]
    arr.sort()
    if arr[0] + arr[1] <= arr[2]:
        return arr[0] + arr[1]
    hasil = 0
    selisih = arr[2] - arr[1]
    arr[2] -= selisih
    arr[0] -= selisih
    hasil += selisih

    return hasil + (arr[1] + arr[0] + arr[2]) // 2


for _ in range(input()):
    n = input()
    print solve(n)