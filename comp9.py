#This code is licensed under UNLICENSE http://unlicense.org
import collections,math,os,sys

#Algorithm:
#Find long periodic sequences in binary string
#that repeat on 1s

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
def bs(b):
	N=math.ceil(math.log(len(c))/math.log(2))
	d={i:_c[0] for i,_c in enumerate(c)}
	return "".join([d[int(b[i:i+N],2)] for i in range(0,len(b),max(1,N))])

#Compress
def c(s):
	c=collections.Counter(s).most_common()
	print(c)
	return

def main():
	s=open("enwik","r").read()[:1000]
	print(s)
	o=c(s)
	print(o)
	return

if __name__=="__main__":
	f=os.path.basename(__file__)
	if f=="comp9.py":
		main()
		#os.rename("comp9.py","decomp9.py")
	else:
		de()
		os.rename("decomp9.py","comp9.py")
