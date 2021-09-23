from structures.stores.LabelStore import LabelStore
from structures.Timer import Timer

class CookieStore(LabelStore):
	def __init__(self):
		super().__init__(0)
		self._cps = 1
		self._cookieIncrementer = Timer(1, lambda: self.add(self._cps))
		self._cookieIncrementer.start()

	def _restartIncrementer(self):
		self._cookieIncrementer.cancel()
		self._cookieIncrementer = Timer(1, lambda: self.add(self._cps))
		self._cookieIncrementer.start()

	def addCPS(self, amount: int = 1):
		self._cps += amount
		self._restartIncrementer()
	
	def removeCPS(self, amount: int = 1):
		self._cps -= amount
		self._restartIncrementer()
