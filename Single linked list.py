class node:
	def __init__(self,data):
		self.data = data
		self.ref = None

class Linkedlist:
	
	def __init__(self):
		self.head = None
	
	def add_begin(self,data):
		new_node = node(data)
		new_node.ref = self.head
		self.head = new_node
	
	def add_end(self,data):
		new_node = node(data)
		if self.head is None:
			self.head =  new_node
		else:
			n = self.head
			while n.ref != None:
				n = n.ref
			n.ref = new_node
		
	def after_given_node(self,data,x):
		n = self.head
		while n != None:
			if x == n.data:
				break
			n = n.ref
		if n is None:
			print("Not present in linked list")
		else:
			new_node = node(data)
			new_node.ref = n.ref
			n.ref = new_node
		
	def befor_given_node(self,data,x):
		if self.head is None:
			print("Its empty list")
			return 
		if self.head.data == x:
			new_node = node(data)
			new_node.ref = self.head
			self.head = new_node
			return 
		n = self.head
		while n.ref != None:
			if n.ref.data == x:
				break
			n = n.ref
		if n.ref is None:
			print("Not present")
		else:
			new_node = node(data)
			new_node.ref = n.ref
			n.ref = new_node
		

	def printing(self):
			if self.head is None:
				print("Dam! its empty")
			else:
				n = self.head
				while n != None:
					print(str(n.data)+"--->",end="")
					n = n.ref

LL1 = Linkedlist()
LL1.add_begin(65)
LL1.add_begin(90)
LL1.after_given_node(55,65)
LL1.after_given_node(76,55)
LL1.befor_given_node(78,90)
LL1.add_end(87)
LL1.printing()
			