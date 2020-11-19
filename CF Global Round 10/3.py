def solve(arr,n):
    peak_index = []
    peak = -float('inf')
    for i in range(n-1):
        if arr[i]>arr[i+1] and arr[i]>peak:
            peak_index.append(i)
            peak=arr[i]
    if not peak_index:
        return 0
    needed = 0
    # print peak_index
    for j in range(len(peak_index)):
        minss = peak_index[j]+1
        if j == len(peak_index)-1:
            hehe =arr[minss:]
            # print hehe
            hm = min(hehe)
            needed+=(arr[peak_index[j]]-hm)
        else:
            maxss =peak_index[j+1]
            hm = min(arr[minss:maxss])
            needed+=(arr[peak_index[j]]-hm)
        # print hm
        # print needed

    
    return needed


        
    

for _ in range(input()):
    n = input()
    n = int(n)
    arr = map(int,raw_input().split())
    print solve(arr,n)

