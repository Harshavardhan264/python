class A():
	def function1(self):
		print("functoin1 information")
class B():
	def function2(self):
		print("functoin2 information")
class C(A,B):
	def function3(self):
		print("function3 information")
obj = C()
obj.function1()
obj.function2()
obj.function3()

#output
functoin1 information
functoin2 information
function3 information
