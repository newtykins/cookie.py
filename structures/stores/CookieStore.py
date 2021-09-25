from structures.stores.Store import Store
from structures.Timer import Timer
from tkinter import StringVar

"""
A custom store to store data about cookies and handling CPS.
Adds helper methods to increase and decrease the CPS value while automatically updating the incrementer.
"""
class CookieStore(Store):
	def __init__(self):
		super().__init__('Cookies', 0)
		self.cps = 1
		self._cookieIncrementer = Timer(1, lambda: self.add(self.cps))
		self._cookieIncrementer.start()
		self.cpsOutput = StringVar()
		self.cpsOutput.set(self._cpsString())

	def _cpsString(self):
		return 'CPS: %i' % (self.cps)

	"""
	Restarts the incrementer with the latest CPS value.
	"""
	def _restartIncrementer(self):
		self._cookieIncrementer.cancel()
		self._cookieIncrementer = Timer(1, lambda: self.add(self.cps))
		self._cookieIncrementer.start()

	"""
	Adds to the CPS value and restarts the incrementer.
	"""
	def addCPS(self, amount: int = 1):
		self.cps += amount
		self.cpsOutput.set(self._cpsString())
		self._restartIncrementer()

	"""
	Removes from the CPS value and restarts the incrementer.
	"""
	def removeCPS(self, amount: int = 1):
		self.cps -= amount
		self.cpsOutput.set(self._cpsString())
		self._restartIncrementer()
