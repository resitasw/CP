def solve(arr,k):
    m = max(arr)
    arr_0 = []
    arr_1 = []
    for i in range(len(arr)):
        arr_1.append(m-arr[i])
    m_2 = max(arr_1)
    for j in range(len(arr)):
        arr_0.append(m_2-arr_1[j])
    
    if k%2==1:
        hasl = ' '.join(map(str,arr_1))
    else:
        hasl = ' '.join(map(str,arr_0))
    return hasl

    
for _ in range(input()):
    n,k = raw_input().split()
    k = int(k)
    arr = map(int,raw_input().split())
    print solve(arr,k)

