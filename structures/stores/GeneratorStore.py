from structures.Stores import LabelStore, CookieStore

class GeneratorStore(LabelStore):
	def __init__(self, cps: int):
		super().__init__(0)
		self._cpsPerUnit = cps

	def add(self, cookieStore: CookieStore, amount: int = 1):
		super().add(amount)
		cookieStore.addCPS(self._cpsPerUnit * amount)
