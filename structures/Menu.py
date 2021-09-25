from structures.Stores import CookieStore, GeneratorStore
from tkinter import Menu as TkMenu

class Menu(TkMenu):
	def __init__(self, master, cookieStore: CookieStore, generatorStores: list[GeneratorStore]):
		super().__init__(master=master)
		self.cookieStore = cookieStore
		self.generatorStores = generatorStores
		# Create the Game menu
		gameMenu = TkMenu(self, tearoff=0)
		gameMenu.add_command(label="New", command=self.newGame)
		self.add_cascade(label='Game', menu=gameMenu)

	"""
	Reset the game to its base state
	"""
	def newGame(self):
		for generator in self.generatorStores:
			generator.remove(generator.quantity)
		self.cookieStore.remove(self.cookieStore.quantity)
		self.cookieStore.removeCPS(self.cookieStore._cps - 1)
