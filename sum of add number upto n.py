#sum of odd numbers upto n
n=int(input("enter number:"))
i=1
sum=0
while(i<=n):
	if(i%2==1):
		sum+=i
	i+=1
print(sum)