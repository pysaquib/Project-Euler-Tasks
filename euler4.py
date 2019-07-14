def palindrome(num):
	n = str(num)
	x = list(n)
	if(x==x[::-1]):
		return True
palindrome(353)

l = []
m = 0
i = 999
while(i>=100):
	j = 999
	while(j>=100):
		p = i*j
		if(palindrome(p)):
			if(p>m):
				m = p
		j-=1
	i-=1
print(m)
