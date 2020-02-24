s=input()
w=input()
a=[]
for i in s:
	if i in w:
		if i not in a:
			a.append(i)
			print (i,end=",")
