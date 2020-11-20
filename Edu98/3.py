def solve(ini):
    normal = 0
    siku = 0
    ans = 0
    for i in ini:
        if i == '(':
            normal += 1
        elif i == '[':
            siku += 1
        elif i == ')' and normal>0:
            normal -= 1
            ans +=1
        elif i == ']' and siku>0:
            siku -= 1
            ans +=1
    return ans




for _ in range(input()):
    ini = raw_input()
    
    print solve(ini)