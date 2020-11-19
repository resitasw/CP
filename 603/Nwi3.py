from sys import stdout
def solve():
    n = int(raw_input())
    ans = []
    i = 1
    while 1:
        ans.append(n / i)
        if not ans[-1]:
            break
        i = n / (n / i) + 1
    ans.reverse()
    stdout.write(str(len(ans)) + '\n')
    stdout.write(' '.join(map(str, ans)))
    stdout.write('\n')
t = int(raw_input())
for _ in xrange(t):
    solve()