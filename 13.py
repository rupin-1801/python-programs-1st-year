def less(a,i,k,r):
	for i in range((len(a)/2)+2):
		if a[i]>k:
			a[i]-=k
			r+=k
		break
def remove(a,i,k,r):
	if a[i]%k!=0:
		a[i]-=1
		r+=1
		remove(a,i,k,r)
def insert(a,i,k,r):
	if a[i]%k!=0:
		if r>0:
			a[i]+=1
			r-=1
			insert(a,i,k,r)
		else:
			less(a,i,k,r)
			insert(a,i,k,r)
	else:
		return r
t=int(input())
while t>0:
	l=list(map(int,input().split()))
	n,k=l[0],l[1]
	a=list(map(int,input().split()))
	r=0
	for i in range((int(len(a)/2))+2):
		remove(a,i,k,r)
	for i in range((int(len(a)/2)+2),len(a)):
		r=insert(a,i,k,r)
	print(r)
	t-=1
	
