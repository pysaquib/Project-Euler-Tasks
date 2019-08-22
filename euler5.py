import fractions
i = 1
lcm = 1
while(i<=20):
    lcm = (lcm*i)/fractions.gcd(lcm, i)
    i+=1
print(int(lcm))
