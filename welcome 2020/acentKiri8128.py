import sys

input = lambda: sys.stdin.readline().rstrip()


def chk(L):
    f = 0
    for i in range(1, L[0]):
        if L[i + 1] > L[i]:
            return (1000001, -1)
    return (L[1], L[-1])


N = int(input())
X = [0] * 1000002
Y = []
for _ in range(N):
    A = [int(a) for a in input().split()]
    a, b = chk(A)
    X[a] += 1
    Y.append(b)

for i in range(1000001)[::-1]:
    X[i] += X[i + 1]

ans = 0
for y in Y:
    ans += X[y + 1]
print(ans)
