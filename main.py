import collections,lzma,sys,tqdm

s=open("enwik9","r").read()
words=s.split(" ")
word_set=[c[0] for c in collections.Counter(words).most_common()]
c=[chr(i) for i in range(3223)]
tc=[None]*len(c)**2
i=0
for c1 in c:
	for c2 in c:
		tc[i]=c1+c2
		i+=1
tc=sorted(tc,key=sys.getsizeof)[:len(word_set)]
f={word:i for i,word in enumerate(word_set)}
w=[None]*len(words)
for i,word in tqdm.tqdm(enumerate(words),total=len(words)):
	w[i]=tc[f[word]]

w="".join(w)
T=int(len(w)/2)
w=w[:T]+w[T:]
ws=" ".join(word_set)
h=list(set([chr(i) for i in range(1114111)])-set(s))
i=0
n=[
"http://www.",
"http://",
".com",
".org",
"https://",
"&quot;",
"&amp;"
]
f=open("w","w")
f.write(ws)
f.close()

r=w+ws
#print(len(lzma.compress(r.encode("utf-8","replace"),preset=9))/len(s))
