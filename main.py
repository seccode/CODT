
import collections
import random
import sys

_m={
"0":"0000",
"1":"0001",
"2":"0010",
"3":"0100",
"4":"1000",
"5":"0011",
"6":"0110",
"7":"1100",
"8":"0101",
"9":"1010"
}

def s2i(s):
	c=collections.Counter(s).most_common()
	print(c)
	a
	n=""
	return n

def i2s(n):
	s=""
	return s

def c(n):
	b="".join([_m[_n] for _n in n])
	return None

def d(o):
	return None

def m():
	s=open("enwik9","r").read()
	print(sys.getsizeof(s))

	n=s2i(s)

	o=c(n)
	print(sum([sys.getsizeof(item) for item in obj]))

	_n=d(o)

	_s=i2s(_n)
	assert _s==s
	return

if __name__=="__main__":
	m()