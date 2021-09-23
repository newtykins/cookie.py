from tkinter import StringVar
from structures.stores.Store import Store

class LabelStore(Store):
	def __init__(self, quantity: int = 0):
		super().__init__(quantity)
		self.output = StringVar()
		self.output.set(0)

	def add(self, amount: int = 1):
		super().add(amount)
		self.output.set(self.quantity)

	def remove(self, amount: int = 1):
		super().remove(amount)
		self.output.set(self.quantity)
