print("Enter your name:",end=" ")
name=input()
print("Welcome to the quiz, Mr.",name)
score=0
l=['What is the correct syntax to output "Hello World" in python?','Which one is NOT a legal variable name?',"Correct Syntax of using dictionary(Assume 'a' is a vaiable):",
	"Which of these are immutable?","What is the correct syntax for range() function?","Which syntax is wrong?","Which of these is not a type of name in programming?",
	"Which is not a type of variable scope?","Choose the incorrect statement:","In which of the data type, we cannot use indexing concept?"]
dic={l[0]:'b',
	l[1]:'d',
	l[2]:'c',
	l[3]:'a',
	l[4]:'b',
	l[5]:'d',
	l[6]:'b',
	l[7]:'a',
	l[8]:'c',
	l[9]:'a',}
opt_a=['p("Hello World")','_myName','dic={a,10;b,20;c,30}','Tupple','range(5,1,2)','print(a,"+",b,"=",c)','Method name','Embeded',"print(l), where 'l' is a list",'Set']
opt_b=['print("Hello World")','My_name','d={a;10:b;20:c;30}','List','range(1,7,1)','print("%d+%d=%d"%(a,b,c))','List name','Built-in',"s=int(input())",'List']
opt_c=['printf("Hello World")','mYName','dic={a:10,b:20,c:30}','String','range(1,9,"a")','print("{}+{}={}".format(a,b,c))','Variable name','Local','print(map(int,s))','Dictionary']
opt_d=['echo "Hello World"','my-name','dic={a,10:b,20:c,30}','Dictionary','range(1,7,-2)','print("{a}+{b}={c}")','Function name','Global','l=list(s.split())','String']
for i in range(len(l)):
	print("\nQues.",i+1,l[i],"\n")
	print("A.",opt_a[i])
	print("B.",opt_b[i])
	print("C.",opt_c[i])
	print("D.",opt_d[i])
	print("\nEnter your Answer(a/b/c/d): ",end=" ")
	ans=input()
	if ans==dic[l[i]]:
		print("\nCorrect Answer,Keep it up")
		score=score+1
	else:
		print("\nSorry, Correct answer is:",dic[l[i]])
		score=score-0.5
	if i!=((len(l))-1):
		print("Your Current Score is:",score)
else:
	print("\nThe End,",end=" ")
	if score==10:
		print("Congrats, Your total score is:",score)
	elif score>=4 and score<=9:
		print("Well done, Your total score is:",score)
	elif score<4:
		print("Better luck next time, Your total score is:",score)