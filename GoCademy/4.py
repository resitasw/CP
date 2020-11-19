from __future__ import division
import math
t = int(raw_input())
for i in range(t):
    a = int(raw_input())
    b = int(raw_input())
    k = int(raw_input())

    hasil = math.floor(b/k)-math.ceil(a/k) + 1
    hasil = int(hasil)
    tes = "Case "+str(i+1)+": "+str(hasil)
    print tes



