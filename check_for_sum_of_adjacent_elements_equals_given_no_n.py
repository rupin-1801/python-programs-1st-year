n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
for i in range(1,len(l)+1):
	if l[i]+l[i-1] ==n:
		print("YES")
		l1=0
		break
	else:
		l1=1
if l1==1:
	print("NO")
