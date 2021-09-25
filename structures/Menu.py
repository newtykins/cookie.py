from structures.GameManager import GameManager
from tkinter import Menu as TkMenu
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pickle

files = [('Cookie.py Save', '*.cookie')]

class Menu(TkMenu):
	def __init__(self, window, manager: GameManager):
		super().__init__(window)
		self.gameManager = manager
		# Create the Game menu
		gameMenu = TkMenu(self, tearoff=0)
		gameMenu.add_command(label='New Game', command=self.newGame)
		gameMenu.add_command(label='Save Game', command=self.saveGame)
		gameMenu.add_command(label='Load Game', command=self.loadGame)
		self.add_cascade(label='Game', menu=gameMenu)

	"""
	Reset the game to its base state
	"""
	def newGame(self):
		for generator in self.gameManager.generators.values():
			generator.remove(generator.quantity)
		self.gameManager.cookies.remove(self.gameManager.cookies.quantity)
		self.gameManager.cookies.removeCPS(self.gameManager.cookies.cps - 1)

	"""
	Save the game using pickle!
	"""
	def saveGame(self):
		# Package the data
		data = {
			'cookies': self.gameManager.cookies.quantity,
			'cps': self.gameManager.cookies.cps,
			'generators': {}
		}
		for key, generator in self.gameManager.generators.items():
			data['generators'][key] = generator.quantity
		# Ask the user where to save the data
		saveFile = asksaveasfilename(filetypes=files, defaultextension=files)
		print(data)
		# Dump it
		with open(saveFile, 'wb') as f:
			pickle.dump(data, f)

	"""
	Load a game file!
	"""
	def loadGame(self):
		saveFile = askopenfilename(filetypes=files, defaultextension=files) # Ask the user for the save file's location
		self.newGame() # Ensure that the game's state is fresh
		# Read the save file
		with open(saveFile, 'rb') as f:
			data = pickle.load(f)
			self.gameManager.cookies.add(data['cookies'])
			self.gameManager.cookies.addCPS(data['cps'] - 1)
			for generatorName, amount in data['generators'].items():
				generator = self.gameManager.generators[generatorName]
				self.gameManager.cookies.removeCPS(generator._cpsPerUnit * amount) # Offset .add()'s default behaviour
				generator.add(amount)
