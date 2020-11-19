
                    

for _ in range(input()):
    n = int(raw_input())
    arr = map(int,raw_input().split())
    for i in range(n):
        if i%2==0:
            # print(2)
            arr[i]=int(0-abs(arr[i]))
        else:
            # print(1)
            arr[i]=int(abs(arr[i]))
    hehe = ' '.join(map(str,arr))
    print(hehe)
