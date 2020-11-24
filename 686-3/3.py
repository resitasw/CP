from collections import defaultdict
def solve(n,arr):
    ans = float('inf')
    dict_index = defaultdict(lambda : [-1])
    for i in range(len(arr)):
        dict_index[arr[i]].append(i)
    # print dict_index
    for j in dict_index:
        minj = 0
        dict_index[j].append(n)
        # print "nyooh"
        # print dict_index[j] 
        for y in range(len(dict_index[j])-1):
            if dict_index[j][y]+1 != dict_index[j][y+1]:
                minj +=1
        
        if minj<ans:
            ans = minj
    return ans


    

for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    print solve(n,arr)
    