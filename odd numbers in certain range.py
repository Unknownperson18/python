#finding odd nubers from certain range
n1=int(input("first number:"))
n2=int(input("last number:"))
while(n1<=n2):
	if(n1%2!=0):
		print(n1,end=" ")
	n1+=1