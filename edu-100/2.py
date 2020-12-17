def solve(n,arr):
    ehe = sum(arr)
    odd = []
    even = []
    sum_odd =0
    sum_even =0
    for i in range(len(arr)):
        if i%2:
            even.append(str(arr[i]))
            odd.append('1')
            sum_odd += abs(1-arr[i])
        else:
            odd.append(str(arr[i]))
            even.append('1')
            sum_even += abs(1-arr[i])
    if sum_even<=sum_odd:
        res = ' '.join(even)
    else:
        res = ' '.join(odd)
    return res




for _ in range(input()):
    hm = input()
    nih = map(int,raw_input().split())
    # res = "1 "*hm
    
    print solve(hm,nih)