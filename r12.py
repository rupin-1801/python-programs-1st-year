s=input("Enter your name:")
print("Welcome Mr. %s to  Python quiz"%(s))
q1="""Q-1: What is the correct Syntax for Dictionary?
	A. dic={1,'b':2,'c'}
 	B. dic={3:'aa';2:34}
 	C. dic={1:'bad',2:'good'}
 	D. d={'e';'f',3;'p')"""
q2='''Q-2: Find out incorrect statement:
 	A. print("%d + %d is %d".format(a,b,c))
 	B. print("{} + {} is {}"%(a,b,c))
 	C. print("{a} + {b} is {c}")
 	D. print("{} + {} is {}".format(a,b,c))'''
q3='''Q-3: Which is not a type of name?
 	A. variable name
 	B. method name
 	C. key name
 	D. method name'''
score=0
d={q1:'c',q2:'d',q3:'c'}
for i in d:
	print(i)
	s=input("\nWould you like to skip this question(y/n):")
	if s=='y':
		continue
	ans=input("Enter your answer:")
	if ans==d[i]:
		print("correct answer!")
		score=score+1.0
	else:
		print("Wrong answer!")
		print("Correct answer is :",d[i])
		score=score-0.5
	print("Your current Score is:",score)
	s=input("Do you want to quit(y,n):")
	if s=='y':
		break
print("The end, thanks for participating in quiz,Your total score is:",score)
