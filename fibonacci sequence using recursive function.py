def fib(n):
	if n<=1:
		return n
	else:
		return (fib(n-1)+fib(n-2))
n=int(input("Enter n value:"))
if n <= 0:
	print("enter positive number")
else:
	print("Fibonacci sequence:")
	for i in range(n):
		print(fib(i))

#output
Enter n value:5
Fibonacci sequence:
0
1
1
2
3
