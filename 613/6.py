n = int(raw_input())
pos = map(int,raw_input().split())
speed = map(int,raw_input().split())
hasil = 0

for i in xrange(n):
    for j in xrange(i+1,n):
        if pos[i]>=pos[j]:
            if speed[i]>=speed[j]:
                hasil+=(pos[i]-pos[j])
        else:
            if speed[j]>=speed[i]:
                hasil+=(pos[j]-pos[i])
print int(hasil)

