def solve(arr_a,arr_b):
    hasil = 0

    # 1-0
    nih = min(arr_a[1],arr_b[0])
    arr_a[1] -= nih
    arr_b[0] -= nih

    # 1 - 1
    nih = min(arr_a[1],arr_b[1])
    arr_a[1] -= nih
    arr_b[1] -= nih

    # 2-1
    nih = min(arr_a[2],arr_b[1])
    arr_a[2] -= nih
    arr_b[1] -= nih
    hasil += (nih*2)

    # 2-2
    nih = min(arr_a[2],arr_b[2])
    arr_a[2] -= nih
    arr_b[2] -= nih

    # 2-0 
    nih = min(arr_a[2],arr_b[0])
    arr_a[2] -= nih
    arr_b[0] -= nih

    # 0-2
    nih = min(arr_a[0],arr_b[2])
    arr_a[0] -= nih
    arr_b[2] -= nih

    # 0 -0
    nih = min(arr_a[0],arr_b[0])
    arr_a[0] -= nih
    arr_b[0] -= nih

    # 0-1 
    nih = min(arr_a[0],arr_b[1])
    arr_a[0] -= nih
    arr_b[1] -= nih

    # 1 - 2
    nih = min(arr_a[1],arr_b[2])
    arr_a[1] -= nih
    arr_b[2] -= nih
    hasil -= (nih*2)

    return hasil

for _ in range(input()):
    arr_a = map(int,raw_input().split())
    arr_b = map(int,raw_input().split())
    print solve(arr_a,arr_b)

