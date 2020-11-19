n,m = map(int,raw_input().split())
x_rob = [0]*n
y_rob = [0]*n
x_light = [0]*m
y_light = [0]*m

cahaya_x = {}
cahaya_y = {}

for i in range(n):
    x_rob[i],y_rob[i]=map(int,raw_input().split())
for i in range(m):
    x_light[i],y_light[i]=map(int,raw_input().split())
    


for i in range(max(x_light)+1):
    cahaya_x[i]=0
for i in range(max(y_light)+1):
    cahaya_y[i]=0
for i in range(m):
    for j in range(x_light[i]+1):
        cahaya_y[j] = max(cahaya_y[j],y_light[i])
for i in range(m):
    for j in range(y_light[i]+1):
        cahaya_x[j] = max(cahaya_x[j],x_light[i])





res = min(max(x_light)-min(x_rob),max(y_light)-min(y_rob))
print(res)