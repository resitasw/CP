def solve(n):
    ans = str(n)
    for i in range(n):
        if i!=0:
            ans = ans + " "+str(i)
    return ans



for _ in range(input()):
    n = input()
    
    print solve(n)
    