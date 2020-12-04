def solve(a,b):
    counter = 0
    a_n = [False]*101
    b_n = [False]*101
    for i in a:
        a_n[i]=True
    for j in b:
        b_n[j]=True
    for k in range(101):
        if a_n[k] and b_n[k]:
            counter+=1
    return counter


for _ in range(input()):
    m,n = map(int,raw_input().split())
    a = map(int,raw_input().split())
    b = map(int,raw_input().split())
    
    print solve(a,b)
    