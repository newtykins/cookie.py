from structures import stores

generatorData = {
	'grandmas': {
		'cost': 10,
		'cps': 2
	}
}

class GameManager:
	def __init__(self):
		self.cookies = stores.CookieStore()
		self.generators = {}
		for name, data in generatorData.items():
			self.generators[name] = stores.GeneratorStore(self.cookies, name.capitalize(), data['cost'], data['cps'])
