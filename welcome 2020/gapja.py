def solve(arr,num,year):
    inde = year%num
    return arr[inde-1]

m,n = raw_input().split()
m= int(m)
n= int(n)
word_m = map(str,raw_input().split())
word_n = map(str,raw_input().split())
t = int(raw_input())
for _ in xrange(t):
    year = int(raw_input())
    hasil = solve(word_m,m,year) + solve(word_n,n,year)
    print hasil