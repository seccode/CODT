import collections,math,random,tqdm
import matplotlib.pyplot as plt
import numpy as np

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

if __name__=="__main__":
	s=open("enwik9","r").read()
	print(len(s))
	g=set()
	for i in tqdm.tqdm(range(0,len(s)-1)):
		g.add(s[i:i+2])
	t=[]
	for i in range(256):
		for j in range(256):
			_t=chr(i)+chr(j)
			if _t not in g:
				t.append(_t)
	c=collections.Counter(s).most_common()[::-1][:len(t)]
	f={_c[0]:_t for _c,_t in zip(c,t)}
	x=list(s)
	del s,t,g,c
	h=set([chr(i) for i in range(256)])
	for i in tqdm.tqdm(range(len(x))):
		if x[i] in f and x[i] not in h:
			x[i]=f[x[i]]
	x="".join(x)
	b,c=sb(x)
	del x
	f=open("b","w")
	f.write(b)
	f.close()
	
