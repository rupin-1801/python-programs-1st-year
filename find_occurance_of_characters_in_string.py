str=input()
l=[]
a=[]
for i in str:
	if i not in l:
		l.append(i)
		a.append(str.count(i))
i=0
j=0
while ((i<len(l)) and (j<len(a))):
	print(l[i],a[j])
	j+=1
	i+=1
