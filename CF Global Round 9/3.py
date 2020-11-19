
                    

for _ in range(input()):
    n = int(raw_input())
    arr = map(int,raw_input().split())
    if len(arr)==1:
        print("YES")
    else:
        if arr[0]>arr[len(arr)-1]:
            print("NO")
        else:
            print("YES")
    # hehe =[arr[0]]
    # for i in range(n-1):
    #     if arr[i]>arr[i+1]:
    #         hehe.append(arr[i+1])
    # if len(hehe)==1:
    #     print("YES")
    # else:
    #     oke = True
    #     for j in range(len(hehe)-1):
    #         if hehe[j+1]<hehe[j]:
    #             oke=False
    #     if oke:
    #         print("YES")
    #     else:
    #         print("NO")
    # hill = []
    # peak = []
    # for i in range(n):
    #     if i == n-1:
    #         peak.append(arr[n-1])
    #         continue
    #     if i ==0:
    #         hill.append(arr[i])
    #     if arr[i]>arr[i+1]:
    #         hill.append(arr[i+1])
    #         peak.append(arr[i])
    # if len(hill)==1:
    #     print("YES")
    # else:
    #     # print("AHAHAHA",hill,peak)
    #     oke = True
    #     mins = hill[0]
    #     maxs = peak[0]
    #     for j in range(len(hill)):
    #         if mins > peak[j]:
    #             oke=False
    #         if (hill[j])<mins:
    #             mins = hill[j]
    #         if (peak[j]>maxs):
    #             maxs=peak[j]
    #     if oke:
    #         print("YES")
    #     else:
    #         print("NO")


            
    
    # # print(hehe)
