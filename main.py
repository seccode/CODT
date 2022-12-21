#This code is licensed under UNLICENSE http://unlicense.org
import collections,math,sys,time

"""
Algorithm idea:
Convert string to binary string and report
locations of 1s with joined indices by constant
spacing. Unjoin and reform string to decompress
"""

#Max string to int conversion length
L=4300

#Convert string to binary string
def s2b(s):
	c=collections.Counter(s).most_common()
	N=math.ceil(math.log(len(c))/math.log(2))
	d={_c[0]:i for i,_c in enumerate(c)}
	_d={}
	for _c in c:
		g="0"*N
		_b=bin(d[_c[0]])[-N:]
		b1,b2=_b.replace("b","0"),_b.replace("b","1")
		b1,b2="0"*(N-len(b1))+b1,"0"*(N-len(b2))+b2
		_d[_c[0]]={1:b1,0:b2}[d[_c[0]]==int(b1,2)]
	b="".join(_d[_s] for _s in s)
	return (b,"".join([_c[0] for _c in c]))

#Convert binary string to string
def b2s(b,c):
	N=math.ceil(math.log(len(c))/math.log(2))
	d={i:_c[0] for i,_c in enumerate(c)}
	s=""
	if N==0:
		s=d[int(b,2)]
	else:
		for i in range(0,len(b),N):
			s+=d[int(b[i:i+N],2)]
	return s

#Compress
def c(b):
	x=[]
	last=0
	for i in range(len(b)):
		if b[i]=="1":
			x.append(i-last)
			last=i
	if len(x)==0:
		m=0
		y=[]
		k=0
	else:
		m=max([len(str(_x)) for _x in x])
		l="".join(["0"*(m-len(str(_x)))+str(_x) for _x in x])
		_y=[l[i:i+L] for i in range(0,len(l),L)]
		k=len(_y[-1])
		y=[int(__y) for __y in _y]
	return (y,k,m,len(b))

#Decompress
def d(y,k,m,n):
	z=[]
	for _y in y[:-1]:
		z.append("0"*(L-len(str(_y)))+str(_y))
	if len(y)!=0:
		z.append("0"*(k-len(str(y[-1])))+str(y[-1]))
		_l="".join(z)
		l=[int(_l[i:i+m]) for i in range(0,len(_l),m)]
		l2=[l[0]]
		for _l in l[1:]:
			l2.append(_l+l2[-1])
	else:
		l2=[]
	b=["0"]*n
	for i in range(n):
		if i in l2:
			b[i]="1"
	return "".join(b)

def main():
	t=time.time()
	enwik9=open("enwik9","rb")
	q=sys.getsizeof(enwik9.read())
	enwik9.close()
	enwik9=open("enwik9","rb")
	#Variable for tracking compressed size
	w=0
	#Read file in chunks
	j=0
	while piece:=enwik9.read(1000000):
		if not piece:
			break
		piece=piece.decode("utf-8")
		#Compress in further chunks
		h=int(len(piece)/400)
		for s in [piece[i:i+h] for i in range(0,len(piece),h)]:
			#String to binary string
			b,_c=s2b(s)
			#Compress
			y,k,m,n=c(b)
			w+=sys.getsizeof(_c)+sys.getsizeof(y)+sys.getsizeof(k)+sys.getsizeof(m)+sys.getsizeof(n)
			#Decompress
			_b=d(y,k,m,n)
			#Binary string to string
			_s=b2s(_b,_c)
			#Decompress(Compress(s))==s
			assert _s==s
		print(time.time()-t)
	#Print compression ratio
	print(w/q)
	enwik9.close()
	print(time.time()-t)
	return

if __name__=="__main__":
	main()
