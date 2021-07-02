#FINDING THE GREATEST NUMBER
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a>b and a>c and a>d):
	print(a,"is greater")
elif(b>a and b>c and b>d):
	print(b,"is greater")
elif(c>a and c>b and c>d):
	print(c,"is greater")
elif(d>a and d>b and d>c):
	print(d,"is greater")
elif(a==b and b==c and c==d):
	print("All numbers are equal")
else:
	print("Greater number eual to any  same numbers")