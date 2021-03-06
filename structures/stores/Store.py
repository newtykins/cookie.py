from tkinter import StringVar

"""
Base store class.
Wraps an integer value with some useful helper methods.
Also provides a StringVar for the value under .output, useful for tkinter.
"""
class Store:
    def __init__(self, name: str, quantity: int = 0):
        self.name = name
        self.quantity = quantity
        self.output = StringVar()
        self.output.set(self._outputString())

    def _outputString(self):
        return '%s: %i' % (self.name, self.quantity)

    """
	Add a specified amount to the stored integer.
	"""
    def add(self, amount: int = 1):
        self.quantity += amount
        self.output.set(self._outputString())

    """
	Remove a specified amount from the stored integer.
	"""
    def remove(self, amount: int = 1):
    	self.quantity -= amount
    	self.output.set(self._outputString())
