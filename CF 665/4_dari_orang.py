#from __future__ import print_function
mod=int(1e9+7)
#import resource
#resource.setrlimit(resource.RLIMIT_STACK, [0x100000000, resource.RLIM_INFINITY])
#import threading
#threading.stack_size(2**25)
#import sys
#sys.setrecursionlimit(10**5)
#fact=[1]
#for i in range(1,100001):
#    fact.append((fact[-1]*i)%mod)
#ifact=[0]*100001
#ifact[100000]=pow(fact[100000],mod-2,mod)
#for i in range(100000,0,-1):
#    ifact[i-1]=(i*ifact[i])%mod
from random import randint as rn
import bisect
from bisect import bisect_left as bl              #c++ lowerbound bl(array,element)
from bisect import bisect_right as br             #c++ upperbound
import itertools
import collections
import math
import heapq
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
def modinv(n,p):
    return pow(n,p-2,p)
def ncr(n,r,p):                        #for using this uncomment the lines calculating fact and ifact
    t=((fact[n])*((ifact[r]*ifact[n-r])%p))%p
    return t
def GCD(x,y):
    while(y):
        x, y = y, x % y
    return x
def ain():                           #takes array as input
    return list(map(int,sin().split()))
def sin():
    return input()
range=xrange
intmax=10**18
intmin=-intmax
"""*******************************************************"""
def main():
    @bootstrap
    def dfs(x,pa):
        s=0
        for i in b[x]:
            if(i==pa):
                continue
            t=yield(dfs(i,x))
            w=t*(n-t)
            l.append(w)
            s+=t
        yield s+1
    for _ in range(int(sin())):
        n=int(sin())
        b=[[] for i in range(n)]
        for i in range(n-1):
            x,y=ain()
            b[x-1].append(y-1)
            b[y-1].append(x-1)
        m=ain()
        p=ain()
        while(len(p)<n-1):
            p.append(1)
        p.sort()
        l=[]
        dfs(0,-1)
        l.sort()
        while(n-1<len(p)):
            x=p.pop()
            p[-1]=(x*p[-1])%mod
        s=0
        for i in range(n-1):
            x=(l[i]*p[i])%mod
            s=(s+x)%mod
        print s
######## Python 2 and 3 footer by Pajenegod and c1729
py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange
 
import os, sys
from io import IOBase, BytesIO
 
BUFSIZE = 8192
class FastIO(BytesIO):
    newlines = 0
    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = "x" in file.mode or "w" in file.mode
        self.write = super(FastIO, self).write if self.writable else None
 
    def _fill(self):
        s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
        self.seek((self.tell(), self.seek(0,2), super(FastIO, self).write(s))[0])
        return s
    def read(self):
        while self._fill(): pass
        return super(FastIO,self).read()
 
    def readline(self):
        while self.newlines == 0:
            s = self._fill(); self.newlines = s.count(b"\n") + (not s)
        self.newlines -= 1
        return super(FastIO, self).readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            self.truncate(0), self.seek(0)
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if py2:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline
        else:
            self.write = lambda s:self.buffer.write(s.encode('ascii'))
            self.read = lambda:self.buffer.read().decode('ascii')
            self.readline = lambda:self.buffer.readline().decode('ascii')
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip('\r\n')
if __name__ == '__main__':
   main()
#threading.Thread(target=main).start()