import collections
import lzma
import math
import random
from tqdm import tqdm

#String to binary string
def sb(s):
    c=collections.Counter(s).most_common()
    N=math.ceil(math.log(len(c))/math.log(2))
    d={_c[0]:i for i,_c in enumerate(c)}
    _d={}
    for _c in c:
        _b=bin(d[_c[0]])[-N:]
        b1,b2=_b.replace("b","0"),_b.replace("b","1")
        b1,b2="0"*(N-len(b1))+b1,"0"*(N-len(b2))+b2
        _d[_c[0]]={1:b1,0:b2}[d[_c[0]]==int(b1,2)]
    return ("".join(_d[_s] for _s in s),"".join([_c[0] for _c in c]))

#Binary string to string
def bs(b,c):
    N=math.ceil(math.log(len(c))/math.log(2))
    d={i:_c[0] for i,_c in enumerate(c)}
    return "".join([d[int(b[i:i+N],2)] for i in range(0,len(b),max(1,N))])

#Compress
def compress(s):
    b,c=sb(s)
    m,last,B,b="",0,len(b),list(b)
    for i in range(1000):
        random.seed(i)
        x=[random.randint(0,1) for _ in range(B)]
        count=sum([1 for j,_x in enumerate(x) if str(_x)==b[j]])
        if count/B>0.52:
            print(i)
            m+=chr(i-last)
            last=i
    return (m,c,B)

#Decompress
def decompress(m,c,B):
    b,last,xs="",0,[]
    for i,_m in enumerate(m):
        last+=ord(_m)
        random.seed(last)
        x=[random.randint(0,1) for _ in range(B)]
        xs.append(x)
    for i in range(B):
        l,r=0,0
        for x in xs:
            if x[i]==0:
                l+=1
            else:
                r+=1
        b+={0:"1",1:"0"}[l>r]
    s=bs(b,c)
    return s

s=open("enwik","r").read()[:500]
m,c,B=compress(s)
s2=m+"@@@"+c+"@@@"+B
print(len(s2)/len(s))

m,c,B=s2.split("@@@")
_s=decompress(m,c,B)
assert _s==s
