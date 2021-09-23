from tkinter import Tk

class Window():
	def __init__(self, title: str, geometry: str = '750x750'):
		self.root = Tk()
		self.root.title(title)
		self.root.geometry(geometry)

	def start(self):
		self.root.mainloop()
