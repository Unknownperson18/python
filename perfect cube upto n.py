n=int(input("select number:"))
i=1
while(n):
	if(i**3>n):
		break
	print(i**3,end="  ")
	i+=1
	