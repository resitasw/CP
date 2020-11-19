from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
def solve(arr):
    if len(arr)==5:
        # print("5 broo")
        product = reduce((lambda x, y: x * y), arr)
        return product
    pos = []
    neg = []
    zeros = 0
    for i in arr:
        if i>0:
            pos.append(i)
        elif i<0:
            neg.append(-i)
        else:
            zeros+=1
    
    if (len(pos)+len(neg))<5:
        return 0
    if (len(pos)+len(neg))==5:
        res = 1
        for i in range(len(pos)):
            res*=pos[i]
        for j in range(len(neg)):
            res *=(-neg[j])
        if res>0:
            return res
        return 0
    
    # pos.sort()
    # neg.sort()
    elif len(pos)==0:
        neg.sort()
        res = -1
        for i in range(5):
            res*=neg[i]
    elif len(pos)==1:
        res = pos[0]
        neg.sort(reverse=True)
        for i in range(4):
            res*=neg[i]
        
    elif len(pos)==2:
        neg.sort(reverse=True)
        pos.sort()
        res = pos[1]
        for i in range(4):
            res*=neg[i]
        
    elif len(pos)<=4:
        if len(neg)>=4:
            res1 = 1
            res3 = 1
            neg.sort(reverse=True)
            pos.sort(reverse=True)
            res1 *= pos[0]
            for i in range(3):
                res3*=pos[i]
            for i in range(4):
                res1 *= neg[i]
                if i<2:
                    res3*=neg[i]
            
            if res1>res3:
                res = res1
            else:
                res = res3
        else:
            # print("kucob")
            neg.sort(reverse=True)
            pos.sort(reverse=True)
            res = 1
            for i in range(3):
                res*=pos[i]

            for i in range(2):
                res *= neg[i]
            
    else:
        
        neg.sort(reverse=True)
        pos.sort(reverse=True)
        res1 = pos[0]
        res3 = 1
        res5 = 1
        for i in range(5):
            if i<3:
                res3*=pos[i]
            res5 *= pos[i]
        if len(neg)>=4:    
            for i in range(4):
                res1 *= neg[i]
                if i<2:
                    res3*=neg[i]
        elif len(neg)>=2:
            res1 = 0
            for i in range(2):
                res3 *= neg[i]
        
        if res5>=res3 and res5>=res1:
            
            res = res5
        elif res3>=res5 and res3>=res1:
            res = res3
        else:
            res = res1
    return res
            


        

for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    print solve(arr)