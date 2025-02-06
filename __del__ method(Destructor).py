class cons:
	def __init__(self):
		self.greet = "Good mng"
	def display(self):
		print("Msg=",self.greet)
	def __del__(self):
		print("object distroyed")
obj = cons()
obj.display()
print(obj)
del obj

#output
Msg= Good mng
<__main__.cons object at 0x7614e0663dc0>
object distroyed

