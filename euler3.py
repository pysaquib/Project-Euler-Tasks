def prime(num):
	i = 2
	c = 0
	while(i<=num**0.5):
		if(num%i==0):
			c+=1
		i+=1
	if(c!=0):
		return False
	else:
		return True
n = 600851475143
c, flag = 0, 0
i = 2
a = []
b = []
while(i<=(n**0.5)):
	if(n%i==0):
		a.append(i)
		flag+=1
	i+=1
for i in a:
	if(prime(i)):
		b.append(i)
print("Largest prime factor of "+str(n)+" is "+str(max(b)))
