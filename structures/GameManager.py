from structures import stores

class GameManager:
	def __init__(self):
		self.cookies = stores.CookieStore()
		self.generators = {
			'grandmas': stores.GeneratorStore(self.cookies, 'Grandmas', 10, 2)
		}
