def solve(arr):
    a = max(arr)
    hehe = {}
    counter = 0
    for i in range(a+1):
        hehe[i] = arr.count(i)
    res = 0
    # print(hehe)
    for j in hehe:
        # print("j",j)
        if counter ==2:
            break
        if hehe[j] == 0:
            if counter==1:
                res+=j
                counter +=1
                
            elif counter==0:
                res+=(j*2)
                counter +=2
            break
        if hehe[j] == 1:
            # print("sama dengan 1")
            if counter==1:
                continue
            elif counter==0:
                res += j
                counter+=1
        else:
            continue
    else:

        # print("masuk else")
        res+= ((a+1)*(2-counter))
    return res

for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    print solve(arr)