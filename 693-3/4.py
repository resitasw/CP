def solve(arr):
    suma = 0
    sumb = 0
    arra = []
    arrb = []
    n = len(arr)
    for i in arr:
        if i%2:
            sumb+= i
            arrb.append(i)
        else:
            suma += i
            arra.append(i)
    arra.sort()
    arrb.sort()
    # print(suma,sumb,arra,arrb)
    for j in range(len(arr)):
        if j != (n-1):
        # alice
            if not j%2:
                if sumb>=suma and arrb:
                    
                    sumb -= arrb[-1]
                    arrb.pop()
                elif arra:
                    arra.pop()
                    
                    
            else:
                if suma>=sumb and arra:
                    suma -= arra[-1]
                    arra.pop()
                elif arrb:
                    arrb.pop()
        else:
            # alice
            
            if (not j%2) and (arrb):
                sumb -= arrb[-1]
            elif j%2 and (arra):
                suma -=arra[-1]
    # print(suma,sumb)
    if suma>sumb:
        return "Alice"
    elif sumb>suma:
        return "Bob"
    else:
        return "Tie"
                

    
    


for _ in range(input()):
    hm = raw_input()
    arr = map(int,raw_input().split())
    
    print solve(arr)