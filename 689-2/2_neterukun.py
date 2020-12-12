import sys
input = sys.stdin.readline
 
 
t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    c = [input()[:-1] for i in range(n)]
 
    c = [[1 if j == "*" else 0 for j in ci] for ci in c]
    ru = [[0] * (m + 1) for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            ru[i][j + 1] = ru[i][j] + c[i][j]
 
    ans = 0
    for i in range(n):
        for j in range(m):
            for k in range(n):
                if not(i + k < n) or j + k + 1 > m or j - k < 0:
                    break
                if ru[i + k][j + k + 1] - ru[i + k][j - k] == 2 * k + 1:
                    ans += 1
                else:
                    break
    print(ans)