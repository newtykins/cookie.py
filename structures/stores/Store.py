class Store:
	def __init__(self, quantity: int = 0):
		self.quantity = quantity

	def add(self, amount: int = 1):
		self.quantity += amount
	
	def remove(self, amount: int = 1):
		self.quantity -= amount
