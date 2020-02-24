n=input()
m=0
for i in range(len(n)):
	if n[i:i+1]==n[-i-1:-i-2:-1]:
		m+=1
	else:
		m-=1
if m==len(n):
	print("Palindrome")
else:
	print("Not palindrome")
