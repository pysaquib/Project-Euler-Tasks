# ProjectEuler
# Sum of even fibonacci terms that doesn't exceed 4 millions
f = 0
s = 1
tSum = 0
while(f<4000000):
	t=f
	f=s
	s=s+t
	if(f%2==0):
		tSum = tSum+f
print(tSum)
