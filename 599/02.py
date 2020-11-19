def solve(a,b):

    for i in range(len(a)):

        for j in range(len(a)):
            arra = list(a)
            arrb = list(b)
            arra[j], arrb[i] = arra[i], arrb[j]
            c = ''.join(arra)
            d = ''.join(arrb)
            if c == d:
                return "YES"
        return "NO"

for _ in range(input()):
    n = input()
    a = input()
    b = input()
    print solve(a,b)

