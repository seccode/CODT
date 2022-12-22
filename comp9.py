#This code is licensed under UNLICENSE http://unlicense.org
import collections,math,os,re,sys

"""
Algorithm idea:
Convert string to binary string and report
locations of 1s with joined indices by constant
spacing. Unjoin and reform string to decompress
"""

#Max string to int conversion length
L=4300

#Store compressed data
A=[]

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
	global A
	enwik9=open("enwik9","rb")
	#Read file in chunks
	while piece:=enwik9.read(1000000):
		if not piece:
			break
		piece=piece.decode("utf-8","ignore")
		#Compress in further chunks
		h=int(len(piece)/400)
		for s in [piece[i:i+h] for i in range(0,len(piece),h)]:
			#String to binary string
			b,_c=s2b(s)
			#Compress
			y,k,m,n=c(b)
			A.append((y,k,m,n,_c))
	enwik9.close()
	f=open(__file__,"r")
	l=f.readlines()
	l=l[:14]+["A={}\n".format(A)]+l[15:]
	f=open(__file__,"w")
	f.writelines(l)
	f.close()
	return

def de():
	global A
	s="".join([b2s(d(_A[0],_A[1],_A[2],_A[3]),_A[-1]) for _A in A])
	f=open("data9","w")
	f.write(s)
	f=open(__file__,"r")
	l=f.readlines()
	l=l[:14]+["A=[]\n"]+l[15:]
	f=open(__file__,"w")
	f.writelines(l)
	f.close()
	return

if __name__=="__main__":
	f=os.path.basename(__file__)
	if f=="comp9.py":
		main()
		os.rename("comp9.py","archive9.py")
	else:
		de()
		os.rename("archive9.py","comp9.py")