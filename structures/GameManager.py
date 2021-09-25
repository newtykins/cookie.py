from structures.Stores import CookieStore, GeneratorStore

class GameManager:
	def __init__(self):
		self.cookies = CookieStore()
		self.generators = {
			'grandmas': GeneratorStore(self.cookies, 'Grandmas', 10, 2)
		}
