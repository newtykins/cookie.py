from structures.Stores import Store, CookieStore

"""
A custom store to store data about generators.
Extends base methods to automatically increment and decrement the CookieStore's CPS accordingly.
"""
class GeneratorStore(Store):
	def __init__(self, cps: int):
		super().__init__(0)
		self._cpsPerUnit = cps

	def add(self, cookieStore: CookieStore, amount: int = 1):
		super().add(amount)
		cookieStore.addCPS(self._cpsPerUnit * amount)

	def remove(self, cookieStore: CookieStore, amount: int = 1):
		super().remove(amount)
		cookieStore.removeCPS(self._cpsPerUnit * amount)
