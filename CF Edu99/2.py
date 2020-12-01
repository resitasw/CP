
def solve(n):
    jump = 0
    addition = 1
    ans = 0
    while ans<n:
        ans += addition
        addition +=1
        jump +=1
    if ans-n-1:
        return jump
    jump +=(abs(n-ans))
    return jump



    
    


for _ in range(input()):
    n = input()
    print solve(n)
    