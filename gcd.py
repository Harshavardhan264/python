def gcd(a,b):
	if b==0:
		return 0
	else:
		while b:
			a,b=b,a%b
		return a
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print("gcd of ",a,b,"is:",gcd(a,b))

#output
enter a value:6
enter b value:2
gcd of  6 2 is: 2
